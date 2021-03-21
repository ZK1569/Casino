import os
from random import randrange
import math

port_monnaie = int(input("Combien voulez-vous avoir sur votre port-monnaie en $: "))


while True:
    nbrChoisi = int(input("Sur quel numero voulez-vous miser: "))
    somme = int(input("Combien d'$ voulez-vous miser: "))
    nbrVictoir = randrange(50)
    valid = True
    
    if 0 <= nbrChoisi <= 50:
        nbrOK = True
    else:
        nbrOK = False
    if nbrOK == False:
        print("""Vous n'avez pas donné un nombre entre 0 et 50 donc réessayer.""") 
        continue
    
    if somme > port_monnaie:
        valid = False

    if valid == False:
        print("Vous ne disposez pas de cette somme. Vous avez",port_monnaie,"veuillez donc rentrer un somme possible.")
        continue
    
    port_monnaie -= somme
    
    
    if nbrChoisi == nbrVictoir:  
        victoir = somme * 3
        port_monnaie += victoir
        print("Le numero gagniant est le", nbrVictoir,"donc vous avez gagnié,")
        print("On va donc ajouter",victoir,"sur votre port-monnaie.")
    else:
        print("Le numero gagniant est le", nbrVictoir,)
        print("Vous avez perdu donc vous perder votre mise de",somme,"$")
        if nbrChoisi % 2 == nbrVictoir % 2:
            victoir = somme / 2
            port_monnaie += math.ceil(victoir)
            print("Mais votre mise a la meme couleur que le numero gagniant donc vous")
            print("recuperez 50% de votre mise.(",math.ceil(victoir),")")
        
    print("Vous disposez maintenant de", port_monnaie,'$.')
    print("---------------Nouvelle partie------------------")
    
    
    
    
    
    