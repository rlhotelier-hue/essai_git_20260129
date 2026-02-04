from calculs import calculer_moyenne, calculer_max

def test_moyenne_standard():
    # On prépare une liste de test
    donnees = [10, 20, 30]
    # On appelle la fonction et on "affirme" (assert) le résultat attendu
    assert calculer_moyenne(donnees) == 20.0

def test_max_standard():
    donnees = [1, 5, 2]
    assert calculer_max(donnees) == 5