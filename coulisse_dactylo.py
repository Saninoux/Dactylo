"""
Partie jouer
"""
# Liste de choses à ajouter:
# - timer
# Bref tout ca c'était pour que tu voies ce que je veux faire 
# Le truc de ecrivez Stop c'est temporaire, après on mettra le timer

import random
import curses

TEXTE = ("""Recopiez le mot et appuyez sur Enter. 
Écrivez Stop quand vous voulez arrêter.""")
LISTE_MOTS_1 = ["roi", "reine", "cheval", "couronne", "nuit", "hiver", "dragon"]
LISTE_MOTS_2 = ["Jon", "Sansa", "Arya", "Daenerys", "Stark", "Lannister", "Targaryen"]
LISTE_MOTS_3 = ["Épée", "Armée", "Trône", "Été", "Traître", "détrôner"]


def jouer_1():   
    """Fonction qui gère le niveau 1."""
    score = 0
    print(TEXTE)
    while True:
        mot = random.choice(LISTE_MOTS_1)
        print("Mot: {}".format(mot))
        reponse = input(">>> ")
        if reponse == mot:
            score += 1
            print("Score: {}".format(score))
        elif reponse == "Stop":
            print("Score final: {}".format(score))
            break 


def jouer_2():
    """Fonction qui gère le niveau 2."""
    score = 0
    print(TEXTE)
    while True:
        mot = random.choice(LISTE_MOTS_2)
        print("Mot: {}".format(mot))
        reponse = input(">>> ")
        if reponse == mot:
            score += 1
            print("Score: {}".format(score))
        elif reponse == "Stop":
            print("Score final: {}".format(score))
            break   
            
            
def jouer_3():
    """Fonction qui gère le niveau 3."""
    score = 0
    print(TEXTE)
    while True:
        mot = random.choice(LISTE_MOTS_3)
        print("Mot: {}".format(mot))
        reponse = input(">>> ")
        if reponse == mot:
            score += 1
            print("Score: {}".format(score))
        elif reponse == "Stop":
            print("Score final: {}".format(score))
            break   


niveau = int(input("Choisis un niveau (1, 2 ou 3): "))
if niveau == 1:
    jouer_1()
elif niveau == 2:
    jouer_2()
elif niveau == 3:
    jouer_3()
