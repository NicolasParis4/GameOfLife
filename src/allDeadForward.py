"""
Obtenir les états menant à tout mort et executant le jeu de la vie sur chaque
état et en checkant si l'état va mener à tout mort
"""

import rules as rl

"""
Fonction récursive permettant d'exécuter le jeu de la vie jusqu'à
tout mort (True) ou un cycle (False)
"""
def rRunGame(rules,state,visited):
    if rules.isDead(rules.next(state)): # condition à modif
        return True
    elif any((rules.next(state) == x).all() for x in visited):
        return False
    else:
        visited.append(state)
        return rRunGame(rules,rules.next(state),visited)

height=input("Hauteur de la grille : ")
width=input("Largeur de la grille : ")
r=rl.Rules(int(height),int(width)) # création d'un objet Rules
result=[] # liste des états menant à tout mort
for state in r.getAll():
    visited=[] # liste des états visités
    if rRunGame(r,state,visited)==True:
        result.append(state)
print(result)
