import time

MOT = "anticonstitutionnellement"


def apprendre():
    for lettre in range(10,len(MOT)+10):
        while True:
            print(MOT[0+lettre-10:lettre+1])
            lettre_tapee = input("tape une lettre: ")
            # quitter le programme
            if lettre_tapee == "1":
                break
            # si touche juste
            elif lettre_tapee == MOT[0+lettre-10]:
                break
            # is touche fausse
            else:
                False


# pour déterminer le temps que le joueur prend pour finir la partie
start = time.time()
apprendre()
end = time.time()
print(end - start + "secondes")


if __name__ == '__main__':
    apprendre()
