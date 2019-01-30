"""
Essai de "curses"
dans Windows, il faut d'abord installer:
    pip install --user windows-curses
"""
import curses


def main(console):
    """
    Fonction principale qui sera "enveloppée" par "curses"
    et aura accès à la console en tant que "console"
    """
    console.clear()
    console.addstr(4, 10, "Bonjour!")
    console.refresh()
    while True: 
        touche = console.getkey()
        console.addstr(6, 10, "Vous avez tapé: {}         ".format(touche))
        if touche == 'q':
            break
    
    
curses.wrapper(main)


