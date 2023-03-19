import random
import string
import mot


YELLOW = (255,255,0) #on défini le jaune pour plus tard
def get_player_input():#on creer une fonction pour stocker les donné de l'utilisateur
    donnee = []

def game_over(): #on creer une fonction pour stopper le jeu
    exit()
def difficulte():
    diff = input("Tapez facile, moyen ou difficile en minuscule: ")  #on demande la difficulté que le user souhaite choisir
    diff = diff.lower() #on met en minuscule au cas ou la personne ne sais pas lire
    #ici on va donné les valeur de la taille du jeu selon la difficulté
    if diff == "facile":
        longueur = 10
        hauteur = 5
    if diff == "moyen":
        longueur = 15
        hauteur = 7
    if diff == "difficile":
        longueur = 30
        hauteur = 15

    #on crée la grille avec des lettres random en majuscule
    grille = [[random.choice(string.ascii_uppercase) for i in range(0, longueur)] for j in range(0, hauteur)]
    print("\n".join(map(lambda row: "  ".join(row), grille))) #on affiche la grille en rajoutant des espaces en chaque debut de lettre ainsi qu'un retour a la ligne pour chaque table(ligne)

def inserer_mot_dans_jeu():
    diff_mot()

def start_game():
    difficulte()
    jeu = true
    if jeu == false :
        game_over()

start_game()