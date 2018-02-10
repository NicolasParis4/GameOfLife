"""
Obtenir tous les états menant à tout mort en partant de l'état tout mort et
en remontant aux états qui mènent à cet état, et en remontant aux états qui
mènent à ces états ...
"""

import rules as rl

r=rl.Rules() # création d'un objet Rules
isEnd=False
result=[r.allDead()] # liste des états menant à tout mort initialisée avec tout mort
while not isEnd:
    isEnd=True
    for state in r.getAll():
        if state in result:
            continue
        elif r.next(state) in result:
            result.append(state)
            isEnd=False
print(result)
