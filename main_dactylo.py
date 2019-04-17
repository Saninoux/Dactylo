"""
Programme dactylo
"""
import curses


def menu(console):
    """Fonction qui affiche menu principal."""
    console.clear()
    console.leaveok(True)
    lignes, colonnes = console.getmaxyx()
    ligne_milieu = lignes // 2
    texte = "Voulez-vous 1) Apprendre ou 2) Jouer?"
    colonne_depart = (colonnes - len(texte)) // 2
    console.addstr(ligne_milieu - 2, colonne_depart, texte)
    
def timer():
    """Fonction qui gère le timer."""
    
    
def apprendre():
    """Fonction qui gère la partie "apprendre"."""
    
   
def jouer():
    """Fonction qui gère la partie "jouer"."""
    

print("Voulez vous:")

if choix == 1:
    apprendre()
    break

elif choix == 2:
    jouer()
    break 
