    
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
Appuyez sur 0 pour quitter pendant le jeu.""")
LISTE_MOTS_1 = ["sera", "forger", "dictionnaire", "entre", "moule", "mecs", "douanier", 
                "effets", "bercez", "institut", "oasis", "persifleur", "sel", "tiens",
                "ramifications", "porter", "lots", "embarquer", "insultant", "publiait",
                "associe", "cabine", "effets", "coca", "phrase", "casquette", "seringue", 
                "chaise", "administrer", "orgelet", "ralentir", "moral", "passer",
                "pomme", "renforcent", "pleurs", "ordinateur", "eucharistie", "tailloir", 
                "baver", "sagace", "clan", "perle", "plombier", "habile", "artiste",
                "perquisitionner", "faille", "intact", "encombrant", "vert", "artistique", 
                "percer", "aspirateur", "tropiques", "influences", "imposer", 
                "chips", "fanfare", "arbre"]
LISTE_MOTS_2 = ["Tony", "Robert", "Steve", "Chris", "Natasha", "Scarlett", "Bruce", "Clint", 
                "Jeremy", "Thor", "Clark", "Henry", "Wayne", "Ben", "Ross", "David", "Chandler",
                "Matthew", "Joey", "Matt", "Rachel", "Jennifer", "Monica", "Courtney", "Phoebe",
                "Lisa", "Homer", "Bart", "Marge", "Maggie", "Abe", "Apu", "Milhouse"]
LISTE_MOTS_3 = ["Épée", "Armée", "Trône", "Été", "Traître", "détrôner"]

print(TEXTE)


def jouer_1():
    """Fonction qui gère le niveau 1."""
    # On initialise le score
    score = 0
    while True:
        # On initialise le compteur
        start = time.time()
        mot = random.choice(LISTE_MOTS_1)
        print("Mot: {}".format(mot))
        reponse = input(">>> ")
        if reponse == mot:
            # On ajoute 1 au score si la réponse est juste
            score += 1
            # tout en indiquant le score actuel
            print("Mots écrits: {}".format(score))
            if score == 30:
                # On arrête le compteur
                end = time.time()
                score_final = end - start
                # On affiche le score final
                print("Vous avez pris {} secondes.".format(score_final))
                break
        # On donne une sortie à l'utilisateur
        elif reponse == "0":
            break
        else:
            # On indique à l'utilisateur qu'il n'a pas eu le point
            print("Faux!")


def jouer_2():
    """Fonction qui gère le niveau 1."""
    score = 0
    while True:
        start = time.time()
        mot = random.choice(LISTE_MOTS_2) # Ici, on prend la liste de mots 
        print("Mot: {}".format(mot))      # avec une difficulté moyenne
        reponse = input(">>> ")
        if reponse == mot:
            score += 1
            print("Mots écrits: {}".format(score))
            if score == 30:
                end = time.time()
                score_final = end - start
                print("Vous avez pris {} secondes.".format(score_final))
                break
        elif reponse == "0":
            break
        else:
            print("Faux!")
            
            
def jouer_3():
    """Fonction qui gère le niveau 1."""
    score = 0
    while True:
        start = time.time()
        mot = random.choice(LISTE_MOTS_3) # Ici, on prend la liste de mots 
        print("Mot: {}".format(mot))      # avec la plus grande difficulté
        reponse = input(">>> ")
        if reponse == mot:
            score += 1
            print("Mots écrits: {}".format(score))
            if score == 30:
                end = time.time()
                score_final = end - start
                print("Vous avez pris {} secondes.".format(score_final))
                break
        elif reponse == "0":
            break
        else:
            print("Faux!")


# On demande un niveau au joueur et on indique quel fonction prendre selon
# son choix
niveau = int(input("Choissisez un niveau (1, 2 ou 3): "))
if niveau == 1:
    jouer_1()
elif niveau == 2:
    jouer_2()
elif niveau == 3:
    jouer_3()
