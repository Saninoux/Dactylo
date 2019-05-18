"""
Menu du jeu dactylographique
dernière modification faite le 14.05.2019
auteurs: JAWDEKAR Aarush et THAY San
"""

import curses
import time

PARTIES = ["Apprendre",  "Jouer     "]


def menu(console):
    """
    Fonction principale qui gère le menu
    """
    console.clear()
    console.leaveok(True)
    nb_lignes, nb_colonnes = console.getmaxyx()
    milieu = nb_lignes // 2
    texte = "Veuillez choisir une option:"
    depart = (nb_colonnes - len(texte)) // 2
    console.addstr(milieu - 2, depart, texte)
    choix = 0
    while True:
        console.addstr(milieu - 1, depart,
                       ">    {}".format(PARTIES[choix]))
        touche = console.getkey()
        if touche == '\n':
            print("Vous avez choisi la partie '{}'".format(PARTIES[choix]))
            break
        elif touche == 'KEY_UP':
            choix -= 1
            if choix < 0:
                choix = len(PARTIES) - 1
            console.addstr(1, 1, 'UP')
        elif touche == 'KEY_DOWN':
            choix += 1
            if choix > len(PARTIES) - 1:
                choix = 0
    return PARTIES[choix]

def appeler():
    choix = curses.wrapper(menu)
    return choix
