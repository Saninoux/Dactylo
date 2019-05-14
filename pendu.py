import random

LISTE_MOTS = ["saucisse", "tortue", "langue", "banane"]

print("Bienvenue au jeu du pendu!")
mot = random.choice(LISTE_MOTS)

essais = ''
chances = 10

while chances > 0:         
    erreurs = 0             
    for lettre in mot:      
        if lettre in essais:    
            print(lettre)
        else:
            print("_")
            erreurs += 1    
    if erreurs == 0:        
        print("Bravo!")
        break 
    essai_demande = input("Devinez une lettre: ") 
    essai = essai_demande.upper()
    essais += essai                    
    if essai not in mot:  
        chances -= 1        
        print("Mauvaise lettre.")
        print("Vous avez {} chance(s) restante(s)".format(chances)) 
        if chances == 0:           
            print("Perdu!")
