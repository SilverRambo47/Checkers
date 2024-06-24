from tkinter import Tk
from checkers_game import CheckersGame

def play_checkers():
    '''play_checkers()
    starts a new game of Checkers'''
    root = Tk()
    root.title('Checkers')
    CG = CheckersGame(root)
    CG.mainloop()

if __name__ == "__main__":
    play_checkers()