"""
Obtenir tous les états menant à mort en partant de l'état tout mort et en
remontant aux états qui mènent à cet état, et en remontant aux états qui
mènent à ces états ...

Il fautait la faire récursive pour que ce soit plus propre ...
"""

import rules as r

isEnd=False
allStates=r.getAll() # touts les états possibles
result=[r.empty()] # liste des états menant à tout mort initialisée avec tout mort
while not isEnd:
    isEnd=True
    for state in allStates:
        if state in result:
            continue
        elif r.next(state) in result:
            result.append(state)
            isEnd=False
