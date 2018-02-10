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
    if rules.next(state)==rules.allDead():
        return True
    elif rules.next(state) in visited:
        return False
    else:
        visited.append(state)
        return rRunGame(rules,rules.next(state),visited)

r=rl.Rules() # création d'un objet Rules
result=[] # liste des états menant à tout mort
for state in r.getAll():
    visited=[] # liste des états visités
    if rRunGame(r,state,visited)==True:
        result.append(state)
print(result)
