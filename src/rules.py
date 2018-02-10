"""
Classe contenant les règles du jeu de la vie
"""

import numpy as np

class Rules():
    length=4
    width=4
    state=np.random.randint(2, size=(length,width))

    def setLength(x):
        self.length=x

    def setWidth(y):
        self.width=y

    def setState(state):
        self.state=state

    def empty():
        return np.zeros((length,width))

    def getAll():
        allStates=[]
        # ...
        return allStates

    def next(state):
        # ...
        return nextState
