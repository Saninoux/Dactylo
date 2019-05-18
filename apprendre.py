"""
Partie "jouer" du jeu dactylographique
dernière modification faite le 14.05.2019
auteurs: JAWDEKAR Aarush et THAY San
"""

import time

MOT = "anticonstitutionnellement"


def apprendre():
    erreur = 0
    for lettre in range(10,len(MOT)+10):
        while True:
            print(MOT[0+lettre-10:lettre+1])
            lettre_tapee = input("tape une lettre: ")
            # quitter le programme
            if lettre_tapee == "1":
                break
            # si touche juste
            elif lettre_tapee == MOT[0+lettre-10]:
                break
            # is touche fausse
            else:
                print("Faux!")
                erreur += 1
                print(erreur)
                False

    return erreur


# pour déterminer le temps que le joueur prend pour finir la partie
def temps_jouee():
    """ fonction permettant au jouer de savoir son temps joué et son
    nombre d'erreurs """
    start = time.time()
    err = apprendre()
    end = time.time()
    temps_jouee = int(round(end - start))
    print("Vous avez pris {}, avec {} erreurs.".format(temps_jouee, err))


def main():
    temps_jouee()


if __name__ == '__main__':
    main()
