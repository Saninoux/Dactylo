

import menu
import curses
import doc_temps_jouee
import doc_jouer

def main():
    # user choisi entre apprendre et jouer
    choix = menu.appeler()
    print(choix)
    if choix == "Apprendre":
        secondes_prises, err = doc_temps_jouee.temps_jouee()
        print("Vous avez pris {} secondes, avec {} erreurs."
              .format(secondes_prises, err))

    else:
        # Aarush, tu dois encore reussir a appliquer cette partie
        vide = doc_jouer.reunificateur()




if __name__ == '__main__':
    main()
