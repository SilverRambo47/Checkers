import numpy as np
from jeu.pion import Pion

class Plateau:
    def __init__(self):
        self.grille = np.zeros((8, 8), dtype=object)
        self.initialiser_pions()

    def initialiser_pions(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 != 0:
                    if i < 3:
                        self.grille[i, j] = Pion("noir")
                    elif i > 4:
                        self.grille[i, j] = Pion("blanc")