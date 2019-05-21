"""
Temps joué et nombre d'erreurs
dernière modification le 21.05.2019
auteurs: JAWDEKAR Aarush, THAY San
"""
import time
import doc_apprendre


def temps_jouee():
    """
    fonction permettant au jouer de savoir son temps joué et son
    nombre d'erreurs.
    """
    start = time.time()
    err = doc_apprendre.appeler_apprendre()
    end = time.time()
    secondes_prises = int(round(end - start))

    return secondes_prises, err


# Pour que la fonction s'annule si elle est exécutée
# intentionellemnt par user
def do_something():
    pass


if __name__=="__main__":
    do_something()
