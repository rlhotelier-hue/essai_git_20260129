# 1. On importe la classe (le moule), pas les fonctions
from analyseur_classe import AnalyseurStatistique
import pandas as pd

def test_donner_moyenne():
    # 2. On crée une instance (une gaufre spécifique)
    mon_objet = AnalyseurStatistique("fake.csv")
    mon_objet.df = pd.DataFrame({'Prix':[10,20,30]})
    assert mon_objet.donner_moyenne("Prix") == 20.0

def test_donner_max():
    mon_objet = AnalyseurStatistique("fake.csv")
    mon_objet.df = pd.DataFrame({'Prix':[10,20,30]})
    assert mon_objet.donner_max("Prix") == 30

