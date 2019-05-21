"""
Partie "jouer" du jeu dactylographique
dernière modification le 18.05.2019
auteurs: JAWDEKAR Aarush et THAY San
"""

# On importe les modules et textes nécessaires
import random
import niveau_jouer
import timer_pour_jouer
import textes_dactylo

# On définit les fonctions qui seront utilisés


def fonction_jouer():
    """Fonction qui gère le jeu."""
    # On initialise le score
    score = 0
    while True:
        mot = random.choice(LISTE_MOTS_1)
        print("Mot: {}".format(mot))
        reponse = input(">>> ")
        if reponse == mot:
            # On ajoute 1 au score si la réponse est juste
            score += 1
            # tout en indiquant le score actuel
            print("Score: {}".format(score))
            if score == 30:
                break
        # On donne une sortie à l'utilisateur
        elif reponse == "0":
            break
        else:
            # On indique à l'utilisateur qu'il n'a pas eu le point
            print("Faux!")

            
fonction_jouer()
# pour que fonction annuler si la fonction executer
# intentiellemnt par user
# def do_anything():
#     pass
#
#
# if __name__=="__main__":
#     do_anything()

# pour que fonction annuler si la fonction executer
# intentiellemnt par user
#def do_anything():
#    pass
#
#
#if __name__=="__main__":
#    do_anything()
