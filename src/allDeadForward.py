# -*- coding: utf-8 -*-
"""
Obtenir les états menant à tout mort et executant le jeu de la vie sur chaque
état et en checkant si l'état va mener à tout mort
"""

import rules as rl
import time

"""
Fonction récursive permettant d'exécuter le jeu de la vie jusqu'à
tout mort (True) ou un cycle (False)
"""
def rRunGame(rules,state,visited):
    if rules.isDead(rules.next(state)):
        return True
    elif any((rules.next(state) == x).all() for x in visited):
        return False
    else:
        visited.append(state)
        return rRunGame(rules,rules.next(state),visited)

print("[Forward]")
height=input("Hauteur de la grille : ")
width=input("Largeur de la grille : ")
print("*****")
start_time = time.time()
r=rl.Rules(int(height),int(width)) # création d'un objet Rules
result=[] # liste des états menant à tout mort
for state in r.getAll():
    visited=[] # liste des états visités
    if rRunGame(r,state,visited)==True:
        result.append(state)
print("Proportion d'états menant à tout mort :")
print(len(result),"/",2**(int(height)*int(width)))
print("--- %s seconds ---" % (time.time() - start_time))
