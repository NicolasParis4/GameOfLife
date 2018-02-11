"""
Classe contenant les règles du jeu de la vie
"""

import itertools
import numpy as np

class Rules:

    def __init__(self,l=4,w=4):
        self.length=l # longeur grille
        self.width=w # largeur grille
        self._state=np.random.randint(2, size=(l,w)) # random binary matrix l*w

    def _get_state(self):
        return self._state
    def _set_state(self,s):
        self._state=s
    state=property(_get_state, _set_state)

    def allDead(self):
    """
    Fonction retournant l'état tout mort pour une grille l*w
    """
        return np.zeros((self.length,self.width)) # matrix l*w of zeros

    def getAll(self):
    """
    Fonction retournant une liste de tous les états possibles
    pour une grille l*w
    """
        allStates=[]
        # Generate all the combinations as string tuples of length l*w
        seq = itertools.product("01", repeat=self.length*self.width)
        for s in seq:
            # Convert to numpy array and reshape to l*w
            arr = np.fromiter(s, np.int8).reshape(self.length,self.width)
            allStates.append(arr)
        return allStates

    def next(self,state):
    """
    Fonction retournant l'état successeur de state avec les règels 3-4
    """
        # TODO :
        # Fonction retournant l'état successeur de state
        return nextState
