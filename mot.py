easy = ['PIP', 'WEB', 'ZOO', 'RUE']
medium = ['MANGER', 'JOUER', 'ARBRE', 'SOURIS']
hard = ['LABRADOR', 'PORTABLE', 'INTERNET', 'ETUDIER']

mot_trouver = ''

comparateur = []

poubelle_jaune = []

def diff_mot():
    if diff == "facile":
        comparateur = easy
    if diff == "moyen":
        comparateur = medium
    if diff == "difficile":
        comparateur = hard


#on creer une fonction qui verifie si le mot selectionner est bon et dans ce cas la on l'ajoute dans la poubelle
def comparer():
    diff_mot()
    if mot_trouver in comparateur:
        poubelle_jaune.append(mot_trouver)
        comparateur.pop(mot_trouver)
