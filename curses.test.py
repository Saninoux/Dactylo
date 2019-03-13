""" 
curses test
if window:
    pip install (--user) window-curses
"""
import curses


def main(console):
    """
    Fonction principal qui sera envoloppée" par "curses"
    et aura accès à la console en tant que "console"
    """
    console.leaveok(True)
    console.clear()
    console.addstr(4, 10, "Bienvenue au jeu de dactylo!")
    console.addstr(5, 10, "Appuie sur 'Q' pour quitter l'application à tout moment.")
    console.refresh()
    while True:
        touche = console.getkey()
        console.addstr(7, 10, "Pour apprendre, tape 1")
        console.addstr(8, 10, "Pour jouer, tape 2")
        touche = console.getkey()
        console.addstr(9, 10, "{}".format(touche))
        if touche == '1':# IMPORT demander niveau
            console.clear()
            console.addstr(4, 10, "Il est conseillé de faire les 15 niveaux progressivement.")
            console.addstr(5, 10, "Par quel niveau souhaites-tu commencer? ")
            demande = False
            while not demande:
                niveau_demande = console.getkey()
                console.addstr(6, 10, "Niveau souhaité: {}".format(niveau_demande))
                if niveau_demande == "1":
                    demande = True            
        elif touche == '2':
            console.clear()
            console.addstr(4, 10, "Il est conseillé de jouer après s'être entraîné.")
            console.addstr(5, 10, "Quel difficulté de texte souhaites-tu?")
            demande = False
            while not demande:
                niveau_demande = console.getkey()
                console.addstr(6, 10, "Difficulté souhaité: {}".format(niveau_demande))
                if niveau_demande == "1":
                    demande = True
        elif touche == 'q':
            break
            

curses.wrapper(main)
