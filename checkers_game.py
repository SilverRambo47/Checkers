from tkinter import Frame, Label, messagebox
from checkers_square import CheckersSquare

class CheckersGame(Frame):
    '''represents a game of Checkers'''

    def __init__(self, master):
        '''CheckersGame(master)
        creates a new Checkers game'''
        Frame.__init__(self, master, bg='white')
        self.grid()
        self.colors = ('red', 'white')
        self.firstClick = ()
        self.jump = [False]
        self.jumpSquares = []
        self.board = {}
        for row in range(8):
            for column in range(8):
                coords = (row, column)
                if row % 2 != column % 2:
                    if row < 3:
                        self.board[coords] = 0
                    elif row > 4:
                        self.board[coords] = 1
                    else:
                        self.board[coords] = None
                else:
                    self.board[coords] = None
        self.currentPlayer = 0
        self.squares = {}
        for row in range(8):
            for column in range(8):
                rc = (row, column)
                self.squares[rc] = CheckersSquare(self, row, column)
                if row % 2 == column % 2:
                    self.squares[rc]['bg'] = 'blanched almond'
                    self.squares[rc].unbind('<Button>')
        self.rowconfigure(8, minsize=3)
        self.turnSquare = CheckersSquare(self, 9, 2)
        self.turnSquare['bg'] = 'gray'
        self.turnSquare.make_color(self.colors[0])
        self.turnSquare.unbind('<Button>')
        Label(self, text='Turn:', font=('Arial', 18)).grid(row=9, column=1)
        for row in range(8):
            for column in range(8):
                rc = (row, column)
                piece = self.get_piece(rc)
                if piece is not None:
                    self.squares[rc].make_color(self.colors[piece])
        
    def get_piece(self, coords):
        '''CheckersBoard.get_piece(coords) -> int
        returns the piece at coords'''
        return self.board[coords]

    def get_player(self):
        '''CheckersBoard.get_player() -> int
        returns the current player'''
        return self.currentPlayer
    
    def get_legal_moves(self, coords):
        '''CheckersBoard.get_legal_moves() -> list
        returns a list of the current player's legal moves'''
        moves = []
        self.jump = [False]
        if self.squares[coords].get_king():
            pivotList = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        elif self.get_piece(coords) == 1:
            pivotList = [(-1, -1), (-1, 1)]
        elif self.get_piece(coords) == 0:
            pivotList = [(1, 1), (1, -1)]
        for pivot in pivotList:
            tempCoords = (coords[0] + pivot[0], coords[1] + pivot[1])
            if tempCoords in self.board.keys():
                if self.get_piece(tempCoords) is None:
                    moves.append(tempCoords)
                elif self.get_piece(tempCoords) == 1 - self.currentPlayer:
                    tempCoords = (coords[0] + 2 * pivot[0], coords[1] + 2 * pivot[1])
                    if tempCoords in self.board.keys():
                        if self.get_piece(tempCoords) is None:
                            self.jump.append(tempCoords)
                            moves.append(tempCoords)
        if len(self.jump) > 1:
            self.jump[0] = True
        return moves
    
    def get_possible_squares(self):
        '''CheckersBoard.get_possible_squares() -> list
        returns a list of the current player's legal cells to click'''
        possibleSquares = []
        self.jumpSquares = []
        for box in self.squares.keys():
            if self.squares[box].get_king():
                pivotList = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
            elif self.currentPlayer == 1:
                pivotList = [(-1, -1), (-1, 1)]
            elif self.currentPlayer == 0:
                pivotList = [(1, 1), (1, -1)]
            for pivot in pivotList:
                tempCoords = (box[0] + pivot[0], box[1] + pivot[1])
                if tempCoords in self.board.keys() and box[0] % 2 != box[1] % 2 and self.get_piece(box) == self.currentPlayer:
                    if self.get_piece(tempCoords) is None and self.get_piece(box) is not None:
                        possibleSquares.append(box)
                    elif self.get_piece(tempCoords) == 1 - self.currentPlayer:
                        tempCoords = (box[0] + 2 * pivot[0], box[1] + 2 * pivot[1])
                        if tempCoords in self.board.keys() and self.get_piece(box) is not None:
                            if self.get_piece(tempCoords) is None:
                                self.jumpSquares.append(box)
                                possibleSquares.append(box)
        return possibleSquares
        
    def next_player(self):
        '''CheckersBoard.next_player()
        advances to next player'''
        self.currentPlayer = 1 - self.currentPlayer
        self.turnSquare.make_color(self.colors[self.currentPlayer])
        
    def get_click(self, event):
        '''CheckersBoard.get_click(event)
        checks a click and acts accordingly'''
        self.check_lose()
        if self.firstClick == ():
            self.firstClick = event.widget.get_position()
            if self.firstClick in self.get_possible_squares() and self.get_piece(self.firstClick) == self.currentPlayer:
                if len(self.jumpSquares) != 0 and self.firstClick not in self.jumpSquares:
                    self.firstClick = ()
                    return
                self.squares[self.firstClick]['highlightthickness'] = 2
                self.squares[self.firstClick]['highlightbackground'] = 'black'
            else:
                self.firstClick = ()
        else:
            self.secondClick = event.widget.get_position()
            if self.secondClick in self.get_legal_moves(self.firstClick):
                if self.jump[0] and self.secondClick not in self.jump:
                    self.check_lose()
                    return
                elif self.jump[0] and self.secondClick in self.jump:
                    self.squares[((self.firstClick[0] + self.secondClick[0]) // 2, (self.firstClick[1] + self.secondClick[1]) // 2)].delete_oval()
                    self.board[((self.firstClick[0] + self.secondClick[0]) // 2, (self.firstClick[1] + self.secondClick[1]) // 2)] = None
                    self.board[self.firstClick] = None
                    self.board[self.secondClick] = self.currentPlayer
                    if self.secondClick[0] == 7 and self.get_piece(self.secondClick) == 0 or self.secondClick[0] == 0 and self.get_piece(self.secondClick) == 1 or self.squares[self.firstClick].get_king():
                        self.squares[self.secondClick].make_king(True)
                        if not self.squares[self.firstClick].get_king():
                            self.squares[self.firstClick].delete_oval()
                            self.squares[self.secondClick].make_color(self.colors[self.currentPlayer])
                            self.squares[self.firstClick]['highlightthickness'] = 0
                            self.get_legal_moves(self.secondClick)
                            self.firstClick = ()
                            self.check_lose()
                            self.next_player()
                            return
                    self.squares[self.firstClick].delete_oval()
                    self.squares[self.secondClick].make_color(self.colors[self.currentPlayer])
                    self.squares[self.firstClick]['highlightthickness'] = 0
                    self.get_legal_moves(self.secondClick)
                    if self.jump[0]:
                        self.firstClick = self.secondClick
                        self.squares[self.firstClick]['highlightthickness'] = 2
                        self.squares[self.firstClick]['highlightbackground'] = 'black'
                        return
                    self.firstClick = ()
                    self.check_lose()
                    self.next_player()
                    return
                self.board[self.firstClick] = None
                self.board[self.secondClick] = self.currentPlayer
                if self.secondClick[0] == 7 and self.get_piece(self.secondClick) == 0 or self.secondClick[0] == 0 and self.get_piece(self.secondClick) == 1 or self.squares[self.firstClick].get_king():
                    self.squares[self.secondClick].make_king(True)
                self.squares[self.firstClick].delete_oval()
                self.squares[self.secondClick].make_color(self.colors[self.currentPlayer])
                self.squares[self.firstClick]['highlightthickness'] = 0
                self.firstClick = ()
                self.check_lose()
                self.next_player()
                    
    def check_lose(self):
        '''CheckersBoard.check_lose(self)
        checks if a player has lost'''
        lose = True
        for box in self.board.keys():
            if self.get_piece(box) == self.currentPlayer:
                if len(self.get_legal_moves(box)) != 0:
                    lose = False
        if lose:
            messagebox.showerror('Checkers', 'Player ' + self.colors[1 - self.currentPlayer] + ' wins', parent=self)
            return
