CHOIX1 = "texte_jf.txt"

ouvrir = open(CHOIX1, "r")
MOT = ouvrir.read()
print(MOT)
ouvrir.close()

n_choice = 1
choice = str("CHOIX") + str(n_choice)
choix_final = str(choice)
print(choix_final)
ouvrir = open(choix_final, "r")
MOT = ouvrir.read()
ouvrir.close()