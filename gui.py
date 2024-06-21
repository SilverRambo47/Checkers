import tkinter as tk
from game import Game
from board import Board
from ai import AI

class GameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jeu de Dames")
        self.game = Game()
        self.board = Board(dimension_sizes=(8, 8))
        self.ai = AI()
        self.game.set_board(self.board)
        self.selected_piece = None
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.draw_board()
        self.draw_pieces()

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = 'white' if (row + col) % 2 == 0 else 'black'
                self.canvas.create_rectangle(col*50, row*50, (col+1)*50, (row+1)*50, fill=color)

    def draw_pieces(self):
        self.canvas.delete("piece")
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row, col]
                if piece != 0:
                    color = 'white' if piece in [1, 3] else 'black'
                    self.canvas.create_oval(col*50+5, row*50+5, col*50+45, row*50+45, fill=color, tags="piece")
                    if piece in [3, 4]:
                        self.canvas.create_oval(col*50+15, row*50+15, col*50+35, row*50+35, fill='gold', tags="piece")

    def on_canvas_click(self, event):
        row, col = event.y // 50, event.x // 50
        if self.selected_piece:
            self.make_move(self.selected_piece, (row, col))
            self.selected_piece = None
        else:
            self.selected_piece = (row, col)

    def make_move(self, start_pos, end_pos):
        try:
            self.game.make_move(start_pos, end_pos)
            self.draw_pieces()
            self.ai_turn()
        except ValueError as e:
            print(e)

    def ai_turn(self):
        self.ai.evaluate_moves(self.board)
        best_move = self.ai.choose_best_move()
        self.game.make_move(*best_move)
        self.draw_pieces()

    def run(self):
        self.root.mainloop()