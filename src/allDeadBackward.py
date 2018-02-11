"""
Obtenir tous les états menant à tout mort en partant de l'état tout mort et
en remontant aux états qui mènent à cet état, et en remontant aux états qui
mènent à ces états ...
"""

import rules as rl

height=input("Hauteur de la grille : ")
width=input("Largeur de la grille : ")
r=rl.Rules(int(height),int(width)) # création d'un objet Rules
isEnd=False
result=[r.allDead()] # liste des états menant à tout mort initialisée avec tout mort
while not isEnd:
    isEnd=True
    for state in r.getAll():
        if any((state == x).all() for x in result):
            continue
        elif r.next(state) in result:
            result.append(state)
            isEnd=False
print(result)
