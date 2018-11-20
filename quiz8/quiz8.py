# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by Jiaquan and Eric Martin for COMP9021


import sys
from random import seed, randrange

from queue_adt import *


def display_grid():
	for i in range(len(grid)):
		print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))


def leftmost_longest_path_from_top_left_corner():
	p = None
	queue = Queue()
	direction = None
	queue.enqueue((direction, [(0, 0)]))
	if grid[0][0] == 0:
		return None
	else:
		while not queue.is_empty():
			direction, p = queue.dequeue()
			i = p[-1][0]
			j = p[-1][1]
			if direction == None:
				if grid[i+1][j] and (i+1,j) not in p:
					queue.enqueue(('S', p+[(i+1, j)]))
				if grid[i][j+1] and (i,j+1) not in p:
					queue.enqueue(('E', p+[(i, j+1)]))
			elif direction == 'N':
				if j<9 and grid[i][j+1] and (i,j+1) not in p:
					queue.enqueue(('E', p+[(i, j+1)]))
				if i>0 and grid[i-1][j] and (i-1,j) not in p:
					queue.enqueue(('N', p+[(i-1, j)]))
				if j>0 and grid[i][j-1] and (i,j-1) not in p:
					queue.enqueue(('W', p+[(i, j-1)]))
			elif direction == 'E':
				if i<9 and grid[i+1][j] and (i+1,j) not in p:
					queue.enqueue(('S', p+[(i+1, j)]))
				if j<9 and grid[i][j+1] and (i,j+1) not in p:
					queue.enqueue(('E', p+[(i, j+1)]))
				if i>0 and grid[i-1][j] and (i-1,j) not in p:
					queue.enqueue(('N', p+[(i-1, j)]))
			elif direction == 'W':
				if i>0 and grid[i-1][j] and (i-1,j) not in p:
					queue.enqueue(('N', p+[(i-1, j)]))
				if j>0 and grid[i][j-1] and (i,j-1) not in p:
					queue.enqueue(('W', p+[(i, j-1)]))
				if i<9 and grid[i+1][j] and (i+1,j) not in p:
					queue.enqueue(('S', p+[(i+1, j)]))
			elif direction == 'S':
				if j>0 and grid[i][j-1] and (i,j-1) not in p:
					queue.enqueue(('W', p+[(i, j-1)]))
				if i<9 and grid[i+1][j] and (i+1,j) not in p:
					queue.enqueue(('S', p+[(i+1, j)]))
				if j<9 and grid[i][j+1] and (i,j+1) not in p:
					queue.enqueue(('E', p+[(i, j+1)]))
		return p
    # Replace pass above with your code


provided_input = input('Enter one integer: ')
try:
	for_seed = int(provided_input)
except ValueError:
	print('Incorrect input, giving up.')
	sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = leftmost_longest_path_from_top_left_corner()
if not path:
	print('There is no path from the top left corner.')
else:
	print(f'The leftmost longest path from the top left corner is: {path}')
           
