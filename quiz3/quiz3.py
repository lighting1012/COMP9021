# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West) and for a given size greater than 1,
# the number of triangles pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1 
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1 
#   1 1
#     1
#
# The output lists, for every direction and for every size, the number of triangles
# pointing in that direction and of that size, provided there is at least one such triangle.
# For a given direction, the possble sizes are listed from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles, that is, obtained
# from the latter by ignoring at least one layer, starting from the base.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict
import copy

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def triangles_in_grid():
	big_dict = defaultdict(list)
	
	nsize = []
	for j in range(0, len(grid)):
		for i in range(0, len(grid)):
			flag = False
			maxsize = min(i + 1, len(grid) - j, len(grid) - i)
			while maxsize >= 2:
				flag = False
				k = 0
				for y in range(j, j + maxsize):
					for x in range(i - k, i + k + 1):
						if grid[y][x] == 0:
							flag = True
							break
					if flag == True:
						maxsize -= 1
						break
					else:
						k += 1
				if flag != True:
					nsize.append(int(maxsize))
					break
	sizekey = sorted(set(nsize), reverse = True)
	for z in range(0, len(sizekey)):
		i = 0
		for zz in range(0, len(nsize)):
			if nsize[zz] == sizekey[z]:
				i += 1
		big_dict['N'].append((sizekey[z], i))
	print('nsize:', nsize)
	
	grid_1 = copy.deepcopy(grid)
	grid_1.reverse()
	grid_2 = [[j[i] for j in grid_1] for i in range(len(grid_1))]
	wsize = []
	for j in range(0, len(grid_2)):
		for i in range(0, len(grid_2)):
			flag = False
			maxsize = min(i + 1, len(grid_2) - j, len(grid_2) - i)
			while maxsize >= 2:
				flag = False
				k = 0
				for y in range(j, j + maxsize):
					for x in range(i - k, i + k + 1):
						if grid_2[y][x] == 0:
							flag = True
							break
					if flag == True:
						maxsize -= 1
						break
					else:
						k += 1
				if flag != True:
					wsize.append(int(maxsize))
					break
	sizekey = sorted(set(wsize), reverse = True)
	for z in range(0, len(sizekey)):
		i = 0
		for zz in range(0, len(wsize)):
			if wsize[zz] == sizekey[z]:
				i += 1
		big_dict['W'].append((sizekey[z], i))
	print('wsize:', wsize)	

	grid_3 = copy.deepcopy(grid_2)
	grid_3.reverse()
	grid_4 = [[j[i] for j in grid_3] for i in range(len(grid_3))]
	ssize = []
	for j in range(0, len(grid_4)):
		for i in range(0, len(grid_4)):
			flag = False
			maxsize = min(i + 1, len(grid_4) - j, len(grid_4) - i)
			while maxsize >= 2:
				flag = False
				k = 0
				for y in range(j, j + maxsize):
					for x in range(i - k, i + k + 1):
						if grid_4[y][x] == 0:
							flag = True
							break
					if flag == True:
						maxsize -= 1
						break
					else:
						k += 1
				if flag != True:
					ssize.append(int(maxsize))
					break
	sizekey = sorted(set(ssize), reverse = True)
	for z in range(0, len(sizekey)):
		i = 0
		for zz in range(0, len(ssize)):
			if ssize[zz] == sizekey[z]:
				i += 1
		big_dict['S'].append((sizekey[z], i))
	print('ssize:', ssize)	

	grid_5 = copy.deepcopy(grid_4)
	grid_5.reverse()
	grid_6 = [[j[i] for j in grid_5] for i in range(len(grid_5))]
	esize = []
	for j in range(0, len(grid_6)):
		for i in range(0, len(grid_6)):
			flag = False
			maxsize = min(i + 1, len(grid_6) - j, len(grid_6) - i)
			while maxsize >= 2:
				flag = False
				k = 0
				for y in range(j, j + maxsize):
					for x in range(i - k, i + k + 1):
						if grid_6[y][x] == 0:
							flag = True
							break
					if flag == True:
						maxsize -= 1
						break
					else:
						k += 1
				if flag != True:
					esize.append(int(maxsize))
					break
	sizekey = sorted(set(esize), reverse = True)
	for z in range(0, len(sizekey)):
		i = 0
		for zz in range(0, len(esize)):
			if esize[zz] == sizekey[z]:
				i += 1
		big_dict['E'].append((sizekey[z], i))
	print('esize:', esize)	
	
	print(big_dict)
	return big_dict
    # Replace return {} above with your code

# Possibly define other functions


try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
triangles = triangles_in_grid()
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')
