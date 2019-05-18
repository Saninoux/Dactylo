"""
Partie "jouer" du jeu dactylographique
dernière modification faite le 14.05.2019
auteurs: JAWDEKAR Aarush et THAY San
"""
import random
import time 

# On définit les constantes
TEXTE = ("""Recopiez le mot qui vous sera donné et appuyez sur Enter. 
Le but du jeu est d'écrire 30 mots dans le moins de temps possible.
Plusieurs niveaux de difficulté vous sont proposés.
Au niveau 3, il vous sera peut-être demandé d'écrire plusieurs mots à la fois.
Appuyez sur 0 pour quitter pendant le jeu.""")
LISTE_MOTS_1 = ["sera", "forger", "dictionnaire", "entre", "moule", "malade", "douanier", 
                "effets", "bercez", "institut", "oasis", "persifleur", "sel", "tiens",
                "ramifications", "porter", "lots", "embarquer", "insultant", "publiait",
                "associe", "cabine", "effets", "coca", "phrase", "casquette", "seringue", 
                "chaise", "administrer", "orgelet", "ralentir", "moral", "passer",
                "pomme", "renforcent", "pleurs", "ordinateur", "eucharistie", "tailloir", 
                "baver", "sagace", "clan", "perle", "plombier", "habile", "artiste",
                "perquisitionner", "faille", "intact", "encombrant", "vert", "artistique", 
                "percer", "aspirateur", "tropiques", "influences", "imposer", 
                "chips", "fanfare", "arbre"]
LISTE_MOTS_2 = ["Tony", "Robert", "Steve", "Chris", "Natasha", "Scarlett", "Bruce", "Mark",
                "Clint", "Jeremy", "Thor", "Clark", "Henry", "Wayne", "Ben", "Ross", 
                "David", "Chandler", "Matthew", "Joey", "Matt", "Rachel", "Jennifer",
                "Monica", "Courtney", "Phoebe", "Lisa", "Homer", "Bart", "Marge", 
                "Maggie", "Abe", "Apu", "Milhouse", "Cristiano", "Lionel", "Roger", "Michael"
                "Jessica", "Luke", "Danny", "Elektra", "Mike", "Lucas", "Dustin", "Eleven"
                "Steve", "Nancy", "Johnathan", "Joyce", "Hopper", "Paul", "Tokyo", "Rio",
                "Moscow", "Denver", "Nairobi", "Helsinki", "Oslo", "Walter", "Jesse", "Jane"
                "Daniel", "Otis", "Jean", "Olga", "Adam", "Harry", "Liam", "Zayn", "Niall"
                "Louis", "Raphael", "Jeff"]
LISTE_MOTS_3 = ["Sébastien Nguyen", "Jéremie Viala", "Daenerys", "Éric", "Dothraki", 
                "anticonstitutionellement", "rhododendron", "parallèle", "Méditerranée", "Pyrénées", 
                "hyperprésidentialisation", "Béatrice", "Léonard", "Mélisandre", "Margaery",
                "Jérôme", "Molière", "Noâm", "Êve", "Yaêl", "Cléopâtre", "César", "Astérix",
                "Obélix", "Abraracourcix", "Assurancetourix", "Cétautomatix", "Odralfabétix",
                "Iélosubmarine", "ménagères", "élèves", "bâtiment", "Castafiore", "Aventurépix"
                "Allégorix", "Déboitementduménix", "Petitélégrafix", "Égyptiens", "Calédoniens",
                "Analgésix", "Iron Man", "Captain America", "Black Widow", "Saint-Étienne",
                "vene, vidi, vici", "Abu Dhabi", "Indonésie", "Brésil", "Saint-Pétersbourg",
                "Severus Rogue", "Nymphadora", "Expelliarmus", "Avada Kedavra", "Obi-Wan Kenobi"
                "Anakin Skywalker", "R2-D2", "C-3PO", "BB-8", "Wingardium Leviosa"]

print(TEXTE)


def jouer():
    """Fonction qui gère le niveau 1."""
    # On initialise le score
    score = 0
    while True:
        mot = random.choice(choix)
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


def choix_niveau():
    niveau = int(input("Choissisez un niveau (1, 2 ou 3): "))
    if niveau == 1:
        mot = LISTE_MOTS_1
    elif niveau == 2:
        mot = LISTE_MOTS_2
    elif niveau == 3:
        mot = LISTE_MOTS_3
    return mot


def temps():
    """Fonction qui gère le timer."""
    start = time.time()
    jouer()
    end = time.time()
    print("Vous avez pris {} secondes.".format(round(end - start)))
    

choix = choix_niveau()
temps()
