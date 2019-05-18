"""
"""


import time
import doc_apprendre


def temps_jouee():
    # pour déterminer le temps que le joueur prend pour finir la partie
    """ fonction permettant au jouer de savoir son temps joué et son
    nombre d'erreurs """
    start = time.time()
    err = doc_apprendre.apprendre()
    end = time.time()
    temps_jouee = int(round(end - start))
    print("Vous avez pris {}, avec {} erreurs.".format(temps_jouee, err))


def main():
    temps_jouee()


if __name__ == '__main__':
    main()
