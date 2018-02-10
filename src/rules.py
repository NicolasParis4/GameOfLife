"""
Classe contenant les règles du jeu de la vie
"""

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
        return np.zeros((self.length,self.width)) # matrix l*w of zeros

    def getAll(self):
        allStates=[]
        # TODO :
        # Fonction retournant une liste de tous les états possibles
        # pour une grille l*w
        return allStates

    def next(self,state):
        # TODO :
        # Fonction retournant l'état successeur de state
        return nextState
