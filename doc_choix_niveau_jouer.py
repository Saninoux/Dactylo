def choix_niveau():
    try:
        mot = "rien"
        niveau = int(input("Choissisez un niveau (1, 2 ou 3): "))
        if niveau == 1:
            liste_choisie = "LISTE_MOTS_1"
        elif niveau == 2:
            liste_choisie = "LISTE_MOTS_2"
        elif niveau == 3:
            liste_choisie = "LISTE_MOTS_3"
    except ValueError:
            print("Ceci n'est pas ce qui était demandé")
            choix_niveau()
    return liste_choisie


# pour que fonction annuler si la fonction executer
# intentiellemnt par user
def do_something():
    pass


if __name__=="__main__":
    do_something()
