# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left corner,
#   so the largest region consisting of connected cells all filled with 1s or
#   all filled with 0s, depending on the value stored in the top left corner;
# - the size of the largest area with a checkers pattern.
#
# Written by Jiquan and Eric Martin for COMP9021

import sys
from random import seed, randint
import copy

dim = 10
grid = [[None] * dim for _ in range(dim)]

def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(dim)))

# Possibly define other functions

try:
    arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density = int(arg_for_seed), int(density)
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()

size_of_largest_homogenous_region_from_top_left_corner  = 0
# Replace this comment with your code
L1 = copy.deepcopy(grid)
def replace_1_by_star(i, j):
	global L1
	if L1[i][j] == 1:
		L1[i][j] = '*'
		if i:
			replace_1_by_star(i-1, j)
		if i < dim - 1:
			replace_1_by_star(i+1, j)
		if j:
			replace_1_by_star(i, j-1)
		if j < dim - 1:
			replace_1_by_star(i, j+1)
def replace_0_by_star(i, j):
	global L1
	if L1[i][j] == 0:
		L1[i][j] = '*'
		if i:
			replace_0_by_star(i-1, j)
		if i < dim - 1:
			replace_0_by_star(i+1, j)
		if j:
			replace_0_by_star(i, j-1)
		if j < dim - 1:
			replace_0_by_star(i, j+1)
if L1[0][0] == 0:
	replace_0_by_star(0, 0)
else:
	replace_1_by_star(0, 0)
#print('L1 is:', L1)

for i in range(dim):
	for j in range(dim):
		if L1[i][j] == '*':
			size_of_largest_homogenous_region_from_top_left_corner += 1
			

print('The size_of the largest homogenous region from the top left corner is '
      f'{size_of_largest_homogenous_region_from_top_left_corner}.'
     )

max_size_of_region_with_checkers_structure = 0
# Replace this comment with your code
L2 = copy.deepcopy(grid)
L3 = []
count = 1
def change_01_to_star(i, j):
	global count
	if L2[i][j] == 0:
		L2[i][j] = '*'
		if i and L2[i-1][j] == 1:
			count += 1
			change_01_to_star(i-1, j)
		if i < dim - 1 and L2[i+1][j] == 1:
			count += 1
			change_01_to_star(i+1, j)
		if j and L2[i][j-1] == 1:
			count += 1
			change_01_to_star(i, j-1)
		if j < dim - 1 and L2[i][j+1] == 1:
			count += 1
			change_01_to_star(i, j+1)
	if L2[i][j] == 1:
		L2[i][j] = '*'
		if i and L2[i-1][j] == 0:
			count += 1
			change_01_to_star(i-1, j)
		if i < dim - 1 and L2[i+1][j] == 0:
			count += 1
			change_01_to_star(i+1, j)
		if j and L2[i][j-1] == 0:
			count += 1
			change_01_to_star(i, j-1)
		if j < dim - 1 and L2[i][j+1] == 0:
			count += 1
			change_01_to_star(i, j+1)
for i in range(dim):
	for j in range(dim):
		count = 1
		change_01_to_star(i, j)
		L3.append(count)
#print('L3 is:', L3)
max_size_of_region_with_checkers_structure = max(L3)
print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
     )




            

