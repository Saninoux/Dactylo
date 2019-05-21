"""
Partie "apprendre" du jeu dactylographique
dernière modification faite le 14.05.2019
auteurs: JAWDEKAR Aarush et THAY San
"""
import doc_demander_niveau
import curses
import time


def apprendre_avec_curses(console):
    """
    Fonction secondaire qui gère "apprendre"
    """
    console.refresh()
    console.leaveok(True)
    console.clear()
    nb_lignes, nb_colonnes = console.getmaxyx()
    milieu = nb_lignes // 2
    depart = (nb_colonnes - len("tape une lettre: ")) // 2
    caractere_entraine = doc_demander_niveau.appeler_niveau()
    erreur = 0
    curses.cbreak()
    for lettre in range(10,len(caractere_entraine)+10):
        while True:
            console.addstr(milieu - 2, depart,
                           caractere_entraine[0+lettre-10:lettre+1] + ' '*6)
            console.addstr(milieu - 3, depart, "|")
            console.addstr(milieu - 1, depart, "|")

            lettre_tapee = console.getch()
            # console.addstr(milieu, depart, "tape une lettre: " + lettre_tapee)
            # quitter le programme
            if lettre_tapee == ord("1") or lettre_tapee == ord("\n"):
                break
            # si touche juste
            elif lettre_tapee == ord(caractere_entraine[0+lettre-10]):
                console.clear()
                console.refresh()
                break
            # is touche fausse
            else:
                # console.addstr(milieu - 4, depart, "Faux!")
                console.clear()
                erreur += 1
                False
    return erreur


def appeler_apprendre():
    """Fonction qui appèle la fonction "apprendre"."""
    erreur = curses.wrapper(apprendre_avec_curses)
    return erreur


def do_anything():
    pass


if __name__=="__main__":
     do_anything()
