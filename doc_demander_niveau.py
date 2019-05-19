"""
"""
CHOIX = [# choix1
          "texte_jf.txt",
          # choix2
          "texte_fghj.txt"
          # choix3
          "texte_dfghjk.txt"
          # choix4
          "texte_sdfghjkl.txt"
          # choix5
          "texte_asdfghjklé.txt"
          # choix6
          "texte_asdfghjklébn.txt"
          # choix7
          "texte_asdfghjklébnvm.txt"
          # choix8
          "texte_asdfghjklébnvmc,.txt"
          # choix9
          "texte_asdfghjklébnvmc,x..txt"
          # choix10
          "texte_asdfghjklébnvmc,x.y-.txt"
          # choix11
          "texte_asdfghjklébnvmc,x.y-.txt"
          # choix12
          "texte_asdfghjklébnvmc,x.y-tz.txt"
          # choix13
          "texte_asdfghjklébnvmc,x.y-tzru.txt"
          # choix14
          "texte_asdfghjklébnvmc,x.y-tzruei.txt"
          # choix15
          "texte_asdfghjklébnvmc,x.y-tzrueiwo.txt"
          # choix16
          "texte_asdfghjklébnvmc,x.y-tzrueiwoqp.txt"
          # choix17
          "texte_caracteres_speciaux"]



def ask_level():
    """
    demander le niveau a l'utilisateur pour 'apprendre'
    """
    while True:
        # Vérifier que user ne donne pas des réponses idiotes
        try:
            n_choice = int(input("choisis un niveau de difficulté: "))
            if n_choice > 17 or n_choice == 0:
                print("Respecte les consignes stp. ")
            else:
                break
        except ValueError:
            print("Respecte les consignes stp. ")
            ask_level()
    ouvrir_fichier = open(CHOIX[n_choice-1], "r")
    MOT = ouvrir_fichier.read()
    ouvrir_fichier.close()

    return MOT


def do_something():
    pass


if __name__=="__main__":
    do_something()
