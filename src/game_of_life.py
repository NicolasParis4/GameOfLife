import random

grid = {}
iteration = 0
n = 8
m = 8

def main():
	iteration = input("Entrez le nombre d'iterations : ")
	grid = game(iterations, n, m, initializeGrid(n,m))


def initializeGrid(n,m):
	grid = [[0] * n for i in range(n)]
	for i in range(n):
	    for j in range(m):
	    	grid[i][j] = random.randint(0, 1)
	 return grid
	#for row in grid:
	#   print(' '.join([str(elem) for elem in row]))

def game(iterations, width, height, grid):
    """
    Implementation of Conway's game of life based on a dictionary as a grid.
    Returns the result grid after running for
    the specified number of iterations.
    """
    for generation in range(iterations):
        # Build a new grid for the next generation.
        # this prevents modified values from affecting calculations before
        # the for loop finished computing all new cell values.
        new_grid = grid.copy()
        print('Running generation', str(generation), '...')

        for cell in grid:
            # Get all the neighbors
            vals_of_neighbors = []
            for neighbor in neighbors(cell, width, height):
                vals_of_neighbors.append(grid[neighbor])

            # Live square dies if it has > 3 or < 2 live neighbors
            if grid[cell] == 1 and \
                (vals_of_neighbors.count(1) > 3 or \
                vals_of_neighbors.count(1) < 2):
                new_grid[cell] = 0

            # Empty square comes to life if it has three live neighbors
            elif grid[cell] == 0 and vals_of_neighbors.count(1) == 3:
                new_grid[cell] = 1

            elif grid[cell] != 1 and grid[cell] != 0:
                raise Exception('Grid can only contain 0 or 1')

    print('Completed simulation after', str(iterations), 'generations.')
    return new_grid



def neighbors(cell, width, height):
	"""
	Returns an array of tuples with all neighbors of the given cell
	"""
	x, y = cell

	return [
	    (x-1 if x-1 >= 0 else width-1, y-1 if y-1 >= 0 else height-1),
	    (x-1 if x-1 >= 0 else width-1, y),
	    (x-1 if x-1 >= 0 else width-1, y+1 if y+1 < height-1 else 0),
	    (x+1 if x+1 < width-1 else 0, y-1 if y-1 >= 0 else height-1),
	    (x+1 if x+1 < width-1 else 0, y),
	    (x+1 if x+1 < width-1 else 0, y+1 if y+1 < height-1 else 0),
	    (x, y-1 if y-1 >= 0 else height-1),
	    (x, y+1 if y+1 < height-1 else 0),
	]


if __name__ == '__main__':
    main()