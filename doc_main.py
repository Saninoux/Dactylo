

import doc_menu
import curses
import doc_temps_jouee
import jouer

def main():
    # user choisi entre apprendre et jouer
    choix = doc_menu.appeler()
    if choix == "Apprendre":
        secondes_prises, err = doc_temps_jouee.temps_jouee()
        print("Vous avez pris {} secondes, avec {} erreurs."
              .format(secondes_prises, err))
    else:
        jouer.activation_fonction()


if __name__ == '__main__':
    main()
