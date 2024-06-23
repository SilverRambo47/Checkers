from tkinter import Canvas

class CheckersSquare(Canvas):
    '''displays a square in the Checkers game'''

    def __init__(self, master, r, c):
        '''CheckersSquare(master, r, c)
        creates a new blank Checker square at coordinate (r, c)'''
        Canvas.__init__(self, master, width=50, height=50, bg='dark green', highlightthickness=0)
        self.grid(row=r, column=c)
        self.position = (r, c)
        self.king = False
        self.bind('<Button>', master.get_click)
        
    def get_king(self):
        '''CheckersSquare.get_king() -> (boolean)
        returns (self.king) attribute of square'''
        return self.king
    
    def make_king(self, boolean):
        '''CheckersSquare.make_king(boolean)
        changes (self.king) attribute of square'''
        self.king = boolean

    def get_position(self):
        '''CheckersSquare.get_position() -> (int, int)
        returns (row, column) of square'''
        return self.position

    def make_color(self, color):
        '''CheckersSquare.make_color(color)
        changes color of piece on square to specified color'''
        ovalList = self.find_all()
        for oval in ovalList:
            self.delete(oval)
        self.create_oval(10, 10, 41, 41, fill=color)
        if self.king:
            self.create_text(25, 30, fill="black", font="Times 40 italic bold", text="*")
        
    def delete_oval(self):
        '''CheckersSquare.delete_color()
        deletes oval on the square'''
        ovalList = self.find_all()
        for oval in ovalList:
            self.delete(oval)
        if self.king:
            self.create_text(25, 30, fill="black", font="Times 40 italic bold", text="")
            self.make_king(False)
