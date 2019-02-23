""" curses test
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
    console.addstr( 4, 10, "Bienvenue au jeu de dactylo!")
    console.addstr( 5, 10, "Appuie sur 'q' pour quitter l'application à tout moment")
    console.refresh()
    while True:
        touche = console.getkey()
        console.addstr(7, 10, "Pour apprendre, tape 1")
        console.addstr(8, 10, "Pour taper du texte, tape 2")
        touche = console.getkey()
        console.addstr(9, 10, "{}".format(touche))
        if touche == '1':# IMPORT demander niveau
            console.clear()
            console.addstr(11, 10, "Il est conseillé de faire les niveaux progressivement. Il en existe 15.")
            console.addstr(13, 10, "Par quel niveau souhaites-tu commencer? ")

            demande = False
            while not demande:
                niveau_demande = console.getkey()
                console.addstr(16, 10, "niveau_demande: {}".format(niveau_demande))

                if niveau_demande == "1":
                    demande = True

        elif touche == '2':# import texte random
            break
        elif touche == 'q':
            break
if __name__ == '__main__':
    curses.wrapper(main)
