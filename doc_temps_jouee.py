"""
"""


import time
import doc_apprendre


def temps_jouee():
    """
    fonction permettant au jouer de savoir son temps joué et son
    nombre d'erreurs.
    """
    start = time.time()
    err = doc_apprendre.apprendre()
    end = time.time()
    secondes_prises = int(round(end - start))

    return secondes_prises, err

def do_something():
    pass

if __name__=="__main__":
    do_something()
