"""
Timer du jeu 
dernière modification le 21.05.2019
auteurs: JAWDEKAR Aarush et THAY San
"""
import jouer_fichier_V2.py
import niveau_jouer
import time


def temps():
    """Fonction qui chronomètre le temps de l'utilisateur."""
    # On démarre le chrono
    start = time.time()
    # On fait jouer l'utilisateur
    jouer_fichier_V2.fonction_jouer()
    # On arrête le chrono lorsque l'utilisateur à fini
    end = time.time()
    # On indique combien de temps l'utilisateur a pris
    print("Vous avez pris {} secondes.".format(round(end - start)))


# Pour que la fonction s'annule si elle est exécutée
# intentionellemnt par user
def do_anything():
    pass


if __name__=="__main__":
    do_anything()
