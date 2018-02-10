"""
Obtenir les états menant à tout mort et executant le jeu de la vie sur chaque
état et en checkant si l'état va mener à tout mort
"""

import rules as r

"""
Fonction récursive permettant d'exécuter le jeu de la vie jusqu'à
tout mort (True) ou un cycle (False)
"""
def rRunGame(state,visited):
    if r.next(state)==r.empty():
        return True
    elif r.next(state) in visited:
        return False
    else:
        visited.append(state)
        return rRunGame(r.next(state),visited)

allStates=r.getAll() # touts les états possibles
result=[] # liste des états menant à tout mort
for state in allStates:
    visited=[] # liste des états visités
    if rRunGame(state,visited)==True:
        result.append(state)
print(result)
