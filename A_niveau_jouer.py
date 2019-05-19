"""
"""
import textes_dactylo
import timer_pour_jouer


def choix_niveau():
    """Fonction qui gère le choix des niveaux."""
    try:
        # valeur bidon
        mot = []
        niveau = "neant"
        # On demande un niveau à l'utilisateur
        niveau = int(input("Choissisez un niveau (1, 2 ou 3): "))
        # On définit la liste de mots en fonction du niveau choisi
        if niveau == 1:
            mot = textes_dactylo.LISTE_MOTS_1
        elif niveau == 2:
            mot = textes_dactylo.LISTE_MOTS_2
        elif niveau == 3:
            mot = textes_dactylo.LISTE_MOTS_3
    # On indique ce qui se passe si l'utilisateur entre des lettres
    except ValueError:
        print("Entrez un chiffre svp!")
        choix_niveau()
    # On indique ce qui se passe si l'utilisateur entre un niveau trop grand
    # ou trop petit
    if niveau < 1 or niveau > 3:
        print("Lisez la consigne attentivement svp!")
        choix_niveau()
    else:
        pass
    return mot



def activation_fonction():
    # On affiche un méssage d'introduction à l'utilisateur
    print(textes_dactylo.TEXTE)
    # On utilise les fonctions pour faire jouer l'utilisateur
    # La fonction "jouer" est déjà dans la fonction "temps"
    choix = choix_niveau()
    timer_pour_jouer.temps()


if __name__=="__main__":
    activation_fonction()
