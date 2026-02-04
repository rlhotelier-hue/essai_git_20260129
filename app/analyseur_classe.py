import pandas as pd

class AnalyseurStatistique:
    def __init__(self, chemin_fichier):
        """Le 'constructeur' : il s'exécute quand on crée l'objet"""
        self.chemin = chemin_fichier
        self.df = None  # On prépare la place pour les données

    def charger_donnees(self):
        try:
            self.df = pd.read_csv(self.chemin)
            print("Données chargées avec succès.")
        except FileNotFoundError:
            print("Erreur : Fichier introuvable.")

    def donner_moyenne(self, colonne):
        if self.df is not None:
            return self.df[colonne].mean()
        return "Erreur : Pas de données chargées."
    
    def donner_max(self, colonne):
        if self.df is not None:
            return self.df[colonne].max()
        return "Erreur : Pas de données chargées"

# --- Utilisation de la classe ---
mon_analyseur = AnalyseurStatistique("data.csv") # Création de l'objet
mon_analyseur.charger_donnees()                  # Appel d'une méthode
print(mon_analyseur.donner_moyenne("Prix"))     # Utilisation des données stockées