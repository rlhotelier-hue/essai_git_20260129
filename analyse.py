import pandas as pd
from calculs import calculer_max
from calculs import calculer_moyenne

def analyse(fichier):
    try:
        df = pd.read_csv("data.csv")
        moyenne = calculer_moyenne(df['Prix'])
        maximum = calculer_max(df['Prix'])
        return moyenne, maximum
    except:
        return "Le fichier n'existe pas"
    
fichier = "data.csv"
results = analyse(fichier)
print ("Bienvenue dans mon premier fichier")    
print (f"Analyse terminée. Moyenne: {results[0]}, Max : {results[0]}")


