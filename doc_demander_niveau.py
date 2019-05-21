"""
"""

import curses


CHOIX = [# choix0
          "texte_jf.txt",
          # choix1
          "texte_fghj.txt",
          # choix2
          "texte_dfghjk.txt",
          # choix3
          "texte_sdfghjkl.txt",
          # choix4
          "texte_asdfghjklé.txt",
          # choix5
          "texte_asdfghjklébn.txt",
          # choix6
          "texte_asdfghjklébnvm.txt",
          # choix7
          "texte_asdfghjklébnvmc,.txt",
          # choix8
          "texte_asdfghjklébnvmc,x..txt",
          # choix9
          "texte_asdfghjklébnvmc,x.y-.txt",
          # choix10
          "texte_asdfghjklébnvmc,x.y-tz.txt",
          # choix11
          "texte_asdfghjklébnvmc,x.y-tzru.txt",
          # choix12
          "texte_asdfghjklébnvmc,x.y-tzruei.txt",
          # choix13
          "texte_asdfghjklébnvmc,x.y-tzrueiwo.txt",
          # choix14
          "texte_asdfghjklébnvmc,x.y-tzrueiwoqp.txt",
          # choix15
          "texte_caracteres_speciaux.txt"]



# def ask_level():
#     """
#     demander le niveau a l'utilisateur pour 'apprendre'
#     """
#     while True:
#         # Vérifier que user ne donne pas des réponses idiotes
#         try:
#             n_choice = int(input("choisis un niveau de difficulté: "))
#             if n_choice >= 15 or n_choice == 0:
#                 print("Respecte les consignes stp. ")
#             else:
#                 break
#         except ValueError:
#             print("Respecte les consignes stp. ")
#             ask_level()
#     ouvrir_fichier = open(CHOIX[n_choice-1], "r")
#     MOT = ouvrir_fichier.read()
#     ouvrir_fichier.close()
#
#     return MOT


# def ask_level(console):
#     """
#     curses
#     demander le niveau a l'utilisateur pour 'apprendre'
#     """
#     console.clear
#     console.leaveok(True)
#     nb_lignes, nb_colonnes = console.getmaxyx()
#     milieu = nb_lignes // 2
#     depart = (nb_colonnes - len("Choisis un niveau de difficulté: ")) // 2
#     while True:
#     # Vérifier que user ne donne pas des réponses idiotes
#         try:
#             console.addstr(milieu, depart, "choisis un niveau de difficulté, ")
#             console.addstr(milieu + 1, depart, "Il en existe 15:")
#             n_choice = console.getkey()
#             n_choice = int(n_choice)
#             if n_choice >= 15 or n_choice == 0:
#                 console.addstr(milieu - 4, depart,
#                                "Respecte les consignes stp. ")
#             else:
#                 break
#         except ValueError:
#             console.addstr(milieu - 4, depart, "Respecte les consignes stp. ")
#             ask_level(console)
#     ouvrir_fichier = open(CHOIX[n_choice-1], "r")
#     MOT = ouvrir_fichier.read()
#     ouvrir_fichier.close()
#
#     return MOT


def ask_level(console):
    """
    Fonction principale qui gère le menu
    """
    console.clear()
    console.leaveok(True)
    nb_lignes, nb_colonnes = console.getmaxyx()
    milieu = nb_lignes // 2
    texte = "Veuillez choisir un niveau:"
    depart = (nb_colonnes - len(texte)) // 2
    console.addstr(milieu - 2, depart, texte)
    choix = 0
    while True:
        console.addstr(milieu - 1, depart,
                       ">    {}                      ".format(CHOIX[choix]))
        touche = console.getkey()
        if touche == '\n':
            console.addstr(milieu-5, depart,
                           "Vous avez choisi la partie '{}'                    "
                           .format(CHOIX[choix]))
            break
        elif touche == 'KEY_UP':
            choix -= 1
            if choix < 0:
                choix = len(CHOIX) - 1
            console.addstr(1, 1, 'UP')
        elif touche == 'KEY_DOWN':
            choix += 1
            if choix > len(CHOIX) - 1:
                choix = 0
    console.clear()
    console.refresh()
    ouvrir_fichier = open(CHOIX[choix], "r")
    MOT = ouvrir_fichier.read()
    ouvrir_fichier.close()
    return MOT

def appeler_niveau():
    choix_niveau = curses.wrapper(ask_level)
    return choix_niveau


# pour que fonction annuler si la fonction executer
# intentiellemnt par user
def do_anything():
    pass


if __name__=="__main__":
     do_anything()
