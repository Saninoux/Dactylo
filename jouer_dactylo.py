"""
Partie jouer
"""
# Liste de choses à ajouter:
# - mots
# - interface curses
import random
import time 

TEXTE = ("""Recopiez le mot et appuyez sur Enter.""")
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


def jouer_1():
    """Fonction qui gère le niveau 1."""
    score = 0
    print(TEXTE)
    while True:
        start = time.time()
        mot = random.choice(LISTE_MOTS_1)
        print("Mot: {}".format(mot))
        reponse = input(">>> ")
        if reponse == mot:
            score += 1
            print("Score: {}".format(score))
            if score == 30:
                end = time.time()
                score_final = round(end - start)
                print("Vous avez pris {} secondes pour écrire 30 mots.".format(score_final))
                break
        else:
            print("Faux!")


def jouer_2():
    """Fonction qui gère le niveau 2."""
    score = 0
    print(TEXTE)
    while True:
        start = time.time()
        mot = random.choice(LISTE_MOTS_2)
        print("Mot: {}".format(mot))
        reponse = input(">>> ")
        if reponse == mot:
            score += 1
            print("Score: {}".format(score))
            if score == 100:
                end = time.time()
                score_final = round(end - start)
                print("Vous avez pris {} secondes pour écrire 100 mots.".format(score_final))
                break
        else:
            print("Réesayez!")
            
            
def jouer_3():
    """Fonction qui gère le niveau 3."""
    score = 0
    print(TEXTE)
    while True:
        start = time.time()
        mot = random.choice(LISTE_MOTS_3)
        print("Mot: {}".format(mot))
        reponse = input(">>> ")
        if reponse == mot:
            score += 1
            print("Score: {}".format(score))
            if score == 100:
                end = time.time()
                score_final = round(end - start)
                print("Vous avez pris {} secondes pour écrire 100 mots.".format(score_final))
                break
        else:
            print("Réesayez!")


niveau = int(input("Choisis un niveau (1, 2 ou 3): "))
if niveau == 1:
    jouer_1()
elif niveau == 2:
    jouer_2()
elif niveau == 3:
    jouer_3()
