import tkinter as tk
from jeu.plateau import Plateau

class JeuDeDames:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Dames")
        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack()
        self.plateau = Plateau()
        self.dessiner_plateau()

    def dessiner_plateau(self):
        for i in range(8):
            for j in range(8):
                x0 = i * 100
                y0 = j * 100
                x1 = x0 + 100
                y1 = y0 + 100
                color = "white" if (i + j) % 2 == 0 else "black"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

        # Appel pour dessiner les pions
        self.dessiner_pions()

    def dessiner_pions(self):
        for i in range(8):
            for j in range(8):
                pion = self.plateau.grille[i][j]
                if pion:
                    x = i * 100 + 50
                    y = j * 100 + 50
                    color = "white" if pion.couleur == "blanc" else "black"
                    self.canvas.create_oval(x - 40, y - 40, x + 40, y + 40, fill=color)