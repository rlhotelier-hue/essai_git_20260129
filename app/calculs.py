def calculer_moyenne(liste_nombres):
    """Calcule la moyenne d'une liste (C'est un docstring)"""
    total = sum(liste_nombres)
    resultat = division_securisee(total, len(liste_nombres))
    return resultat

def calculer_max(liste_nombre):
    total = max(liste_nombre)
    return total

def division_securisee(a, b):
    try:
        resultat = a / b 
        return resultat
    except ZeroDivisionError:
        return "Erreur : On epeut pas diviser par zéro !"

#Utilisation
mes_donnes = [10, 20, 30, 40 ] 
resultat = calculer_moyenne(mes_donnes)
valeur_max = calculer_max(mes_donnes)
print(f"La moyenne est de : {resultat} et le max est de : {valeur_max}")