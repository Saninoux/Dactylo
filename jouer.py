"""
Partie "jouer" du jeu dactylographique
dernière modification faite le 14.05.2019
auteurs: JAWDEKAR Aarush et THAY San
"""

# Liste de choses à ajouter:
# - mots
# - interface curses
# - éviter redondances

import random
import time

# On définit les constantes
TEXTE = ("""Recopiez le mot qui vous sera donné et appuyez sur Enter.
Le but du jeu est d'écrire 30 mots dans le moins de temps possible.
Plusieurs niveaux de difficulté vous sont proposés.
Appuyez sur 0 pour quitter PENDANT le jeu.""")
LISTE_MOTS_1 = ["sera", "forger", "dictionnaire", "entre", "moule", "mecs",
                "douanier", "effets", "bercez", "institut", "oasis",
                "persifleur", "sel", "tiens", "ramifications", "porter",
                "lots", "embarquer", "insultant", "publiait", "associe",
                "cabine", "effets", "coca", "phrase", "casquette", "seringue",
                "chaise", "administrer", "orgelet", "ralentir", "moral",
                "passer", "pomme", "renforcent", "pleurs", "ordinateur",
                "eucharistie", "tailloir", "baver", "sagace", "clan", "perle",
                "plombier", "habile", "artiste", "perquisitionner", "faille",
                "intact", "encombrant", "vert", "artistique", "percer",
                "aspirateur", "tropiques", "influences", "imposer", "chips",
                "fanfare", "arbre"]
LISTE_MOTS_2 = ["Tony", "Robert", "Steve", "Chris", "Natasha", "Scarlett",
                "Bruce", "Mark", "Clint", "Jeremy", "Thor", "Clark", "Henry",
                "Wayne", "Ben", "Ross", "David", "Chandler", "Matthew", "Joey",
                "Matt", "Rachel", "Jennifer", "Monica", "Courtney", "Phoebe",
                "Lisa", "Homer", "Bart", "Marge", "Maggie", "Abe", "Apu",
                "Milhouse"]
LISTE_MOTS_3 = ["Sébastien"]



def jouer():
    """Fonction qui gère le niveau 1."""
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
            print("Mots écrits: {}".format(score))
            if score == 30:
                break
        # On donne une sortie à l'utilisateur
        elif reponse == "0":
            break
        else:
            # On indique à l'utilisateur qu'il n'a pas eu le point
            print("Faux!")


def choix_niveau():
    while True:
        niveau = int(input("Choissisez un niveau (1, 2 ou 3): "))
        try:
            if niveau == '1':
                mot = "LISTE_MOTS_1"
                False
            elif niveau == '2':
                mot = "LISTE_MOTS_2"
                False
            elif niveau == '3':
                mot = "LISTE_MOTS_3"
                False
        except ValueError:
                print("Ceci n'est pas ce qui était demandé")
                True
    return mot


def temps():
    """Fonction qui gère le timer."""
    start = time.time()
    jouer()
    end = time.time()
    print("Vous avez pris {} secondes.".format(round(end - start)))

def main():
    print(TEXTE)
    choix = choix_niveau()
    temps()

if __name__ == '__main__':
    main()
