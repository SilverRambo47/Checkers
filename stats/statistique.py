import pandas as pd
import matplotlib.pyplot as plt

class Statistiques:
    def __init__(self):
        self.data = pd.DataFrame(columns=["partie_id", "joueur", "resultat"])

    def enregistrer_partie(self, partie_id, joueur, resultat):
        self.data = self.data.append({"partie_id": partie_id, "joueur": joueur, "resultat": resultat}, ignore_index=True)

    def visualiser_statistiques(self):
        resultats = self.data["resultat"].value_counts()
        resultats.plot(kind="bar")
        plt.show()