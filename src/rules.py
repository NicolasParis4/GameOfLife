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

    def isDead(self,state):
        return np.array_equal(state,self.allDead())

    def getAll(self):
        """
        Fonction retournant une liste de tous les états possibles
        pour une grille h*w
        """
        allStates=[]
        # Generate all the combinations as string tuples of length h*w
        seq = itertools.product("01", repeat=self.height*self.width)
        for s in seq:
            # Convert to numpy array and reshape to h*w
            arr = np.fromiter(s, np.int8).reshape(self.height,self.width)
            allStates.append(arr)
        return allStates

    def neighbors(self,x,y):
    	"""
    	Returns an array of tuples with all neighbors of the given cell
    	"""
    	return [
    	    (x-1 if x-1 >= 0 else self.width-1, y-1 if y-1 >= 0 else self.height-1),
    	    (x-1 if x-1 >= 0 else self.width-1, y),
    	    (x-1 if x-1 >= 0 else self.width-1, y+1 if y+1 < self.height-1 else 0),
    	    (x+1 if x+1 < self.width-1 else 0, y-1 if y-1 >= 0 else self.height-1),
    	    (x+1 if x+1 < self.width-1 else 0, y),
    	    (x+1 if x+1 < self.width-1 else 0, y+1 if y+1 < self.height-1 else 0),
    	    (x, y-1 if y-1 >= 0 else self.height-1),
    	    (x, y+1 if y+1 < self.height-1 else 0),
    	]

    def next(self,state):
        """
        Fonction retournant l'état successeur de state avec les règels 3-4
        """
        nextState=state.copy()
        for h in range(len(state)):
            for w in range(len(state[h])):
                # Get all the neighbors
                valsOfNeighbors = []
                for neighbor in self.neighbors(w,h):
                    valsOfNeighbors.append(state[neighbor])

                # Cell is alive if 3 or 4 neighbors
                if valsOfNeighbors.count(1) == 3 or valsOfNeighbors.count(1) == 4:
                    nextState[h][w] = 1
                # Cell is dead otherwise
                else:
                    nextState[h][w] = 0
        return nextState
