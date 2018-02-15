# -*- coding: utf-8 -*-
"""
Classe contenant les règles du jeu de la vie
"""

import itertools
import numpy as np

class Rules:

    def __init__(self,h=4,w=4):
        self.height=h # hauteur grille
        self.width=w # largeur grille
        self._state=np.random.randint(2, size=(h,w)) # random binary matrix h*w

    def _get_state(self):
        return self._state
    def _set_state(self,s):
        self._state=s
    state=property(_get_state, _set_state)

    def allDead(self):
        """
        Fonction retournant l'état tout mort pour une grille h*w
        """
        return np.zeros((self.height,self.width)) # matrix h*w of zeros

    def isDead(self,s):
        state = np.fromiter(s, np.int8).reshape(self.height,self.width)
        return np.array_equal(state,self.allDead())

    def getAll(self):
        """
        Fonction retournant une liste de tous les états possibles
        pour une grille h*w
        """
        allStates=[]
        # Generate all the combinations as string tuples of length h*w
        seq = itertools.product(range(2), repeat=self.height*self.width)
        return seq

    def neighbors(self,h,w):
    	"""
    	Returns an array of tuples with all neighbors of the given cell
    	"""
    	return [
    	    (h-1 if h-1 >= 0 else self.height-1, w-1 if w-1 >= 0 else self.width-1),
    	    (h-1 if h-1 >= 0 else self.height-1, w),
    	    (h-1 if h-1 >= 0 else self.height-1, w+1 if w+1 < self.width else 0),
    	    (h+1 if h+1 < self.height else 0, w-1 if w-1 >= 0 else self.width-1),
    	    (h+1 if h+1 < self.height else 0, w),
    	    (h+1 if h+1 < self.height else 0, w+1 if w+1 < self.width else 0),
    	    (h, w-1 if w-1 >= 0 else self.width-1),
    	    (h, w+1 if w+1 < self.width else 0),
    	]

    def next(self,s):
        """
        Fonction retournant l'état successeur de state avec les règles de Conway
        """
        state = np.fromiter(s, np.int8).reshape(self.height,self.width)
        nextState=[]
        for h in range(len(state)):
            for w in range(len(state[h])):
                # Get all the neighbors
                valsOfNeighbors = []
                for neighbor in self.neighbors(h,w):
                    valsOfNeighbors.append(state[neighbor])
                # Live square dies if it has > 3 or < 2 live neighbors
                if state[h][w] == 1:
                    if (valsOfNeighbors.count(1) > 3 or valsOfNeighbors.count(1) < 2):
                        nextState.append('0')
                    else:
                        nextState.append('1')
                # Empty square comes to life if it has three live neighbors
                else:
                    if valsOfNeighbors.count(1) == 3:
                        nextState.append('1')
                    else:
                        nextState.append('0')
        return tuple(nextState)
