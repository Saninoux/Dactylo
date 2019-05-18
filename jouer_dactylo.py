"""
Partie "jouer" du jeu dactylographique
dernière modification le 18.05.2019
auteurs: JAWDEKAR Aarush et THAY San
"""
# On importe les modules et textes nécessaires
import random
import time 
import textes_dactylo

# On affiche un méssage d'introduction à l'utilisateur
print(textes_dactylo.TEXTE)


# On définit les fonctions qui seront utilisés 


def jouer():
    """Fonction qui gère le jeu."""
    # On initialise le score
    score = 0
    while True:
        mot = random.choice(choix)
        print("Mot: {}".format(mot))
        reponse = input(">>> ")
        if reponse == mot:
            # On ajoute 1 au score si la réponse est juste
            score += 1
            # tout en indiquant le score actuel
            print("Score: {}".format(score))
            if score == 30:
                break
        # On donne une sortie à l'utilisateur
        elif reponse == "0":
            break
        else:
            # On indique à l'utilisateur qu'il n'a pas eu le point
            print("Faux!")


def choix_niveau():
    """Fonction qui gère le choix des niveaux."""
    try:
        # On définit niveau et mot comme globales pour ne pas avoir
        # d'erreurs s'il faut gérer les éxceptions
        global niveau
        global mot
        # On demande un niveau à l'utilisateur
        niveau = int(input("Choissisez un niveau (1, 2 ou 3): "))
        # On définit la liste de mots en fonction du niveau choisi
        if niveau == 1:
            mot = textes_dactylo.LISTE_MOTS_1
        elif niveau == 2:
            mot = textes_dactylo.LISTE_MOTS_2
        elif niveau == 3:
            mot = textes_dactylo.LISTE_MOTS_3
    # On indique ce qui se passe si l'utilisateur entre des lettres
    except ValueError:
        print("Entrez un chiffre svp!")
        choix_niveau()
    # On indique ce qui se passe si l'utilisateur entre un niveau trop grand
    # ou trop petit
    if niveau < 1 or niveau > 3:
        print("Lisez la consigne attentivement svp!")
        choix_niveau()
    return mot


def temps():
    """Fonction qui chronomètre le temps de l'utilisateur."""
    # On démarre le chrono
    start = time.time()
    # On fait jouer l'utilisateur
    jouer()
    # On arrête le chrono lorsque l'utilisateur à fini
    end = time.time()
    # On indique combien de temps l'utilisateur a pris
    print("Vous avez pris {} secondes.".format(round(end - start)))
    
    
# On utilise les fonctions pour faire jouer l'utilisateur
# La fonction "jouer" est déjà dans la fonction "temps"
choix = choix_niveau()
temps()
