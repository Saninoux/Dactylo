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
    secondes_prises = int(round(end - start))
    return secondes_prises, err
