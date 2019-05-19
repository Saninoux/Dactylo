"""
Partie "apprendre" du jeu dactylographique
dernière modification faite le 14.05.2019
auteurs: JAWDEKAR Aarush et THAY San
"""
import demander_niveau

# caractere_entraine = "anticonstitutionnellement"


def apprendre():
    caractere_entraine = demander_niveau.ask_level()
    erreur = 0
    for lettre in range(10,len(caractere_entraine)+9):
        while True:
            print(caractere_entraine[0+lettre-10:lettre+1])
            lettre_tapee = input("tape une lettre: ")
            # quitter le programme
            if lettre_tapee == "1" or lettre_tapee == "\n":
                break
            # si touche juste
            elif lettre_tapee == caractere_entraine[0+lettre-10]:
                break
            # is touche fausse
            else:
                print("Faux!")
                erreur += 1
                False

    return erreur


def do_something():
    pass


if __name__=="__main__":
    do_something()
