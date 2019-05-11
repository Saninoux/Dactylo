"""
Partie jouer
"""
import random

# Liste de choses à ajouter:
# - timer
# - mettre ca dans une boucle pour mots illimités et enlever redondance
# Bref tout ca c'était pour que tu voies ce que je veux faire 
# J'ai mis le même truc 5 fois parce que l'utilisateur va entrer plusieurs
# mots donc ca donne un apercu

LISTE_MOTS = ["Stark", "Targaryen", "couteau", "dragon", "roi", "reine"]
score = 0

MOT = random.choice(LISTE_MOTS)
print(MOT)
reponse = input("Recopiez le mot et appuyez sur Enter: ")
if reponse == MOT:
    score += 1
    print("Score: {}".format(score))

MOT = random.choice(LISTE_MOTS)
print(MOT)
reponse = input("Recopiez le mot et appuyez sur Enter: ")
if reponse == MOT:
    score += 1
    print("Score: {}".format(score))

MOT = random.choice(LISTE_MOTS)
print(MOT)
reponse = input("Recopiez le mot et appuyez sur Enter: ")
if reponse == MOT:
    score += 1
    print("Score: {}".format(score))

MOT = random.choice(LISTE_MOTS)
print(MOT)
reponse = input("Recopiez le mot et appuyez sur Enter: ")
if reponse == MOT:
    score += 1
    print("Score: {}".format(score))

MOT = random.choice(LISTE_MOTS)
print(MOT)
reponse = input("Recopiez le mot et appuyez sur Enter: ")
if reponse == MOT:
    score += 1
    print("Score final: {}".format(score))

    
    


