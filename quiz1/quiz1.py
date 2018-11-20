# Written by Jiaquan Xu and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers at most equal to a given upper bound,
of a given length, all controlled by user input.

Outputs four lists:
- elements_to_keep, consisting of L's smallest element, L's third smallest element,
  L's fifth smallest element, ...
  Hint: use sorted(), list slices, and set()
- L_1, consisting of all members of L which are part of elements_to_keep, preserving
  the original order
- L_2, consisting of the leftmost occurrences of the members of L which are part of
  elements_to_keep, preserving the original order
- L_3, consisting of the LONGEST, and in case there are more than one candidate, the
  LEFTMOST LONGEST sequence of CONSECUTIVE members of L that reduced to a set,
  is a set of integers without gaps.
'''

import sys
from random import seed, randint


try:
    arg_for_seed, upper_bound, length = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, upper_bound, length = int(arg_for_seed), int(upper_bound), int(length)
    if arg_for_seed < 0 or upper_bound < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, upper_bound) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)

L_1 = []
L_2 = []
L_3 = []
elements_to_keep = []

elements_to_keep = sorted(set(L))
elements_to_keep = elements_to_keep[0::2]

for i in range(len(L)):
	if elements_to_keep.count(L[i]) > 0:
		L_1.append(L[i])

for i in range(len(L)):
	if elements_to_keep.count(L[i]) > 0:
		if L_2.count(L[i]) == 0:
			L_2.append(L[i])
		

flag = False
for i in range(0, len(L)):
	for k in range(0, i + 1):
		L_3 = L[k:k + len(L) - i]
		if list(sorted(set(L[k:k + len(L) - i])))[-1] - list(sorted(set(L[k:k + len(L) - i])))[0] + 1 == len(list(sorted(set(L[k:k + len(L) - i])))):	
			flag = True
			break
	if flag:
		break
	

		
print('\nThe elements to keep in L_1 and L_2 are:')
print('  ', elements_to_keep)
print('\nHere is L_1:')
print('  ', L_1)
print('\nHere is L_2:')
print('  ', L_2)
print('\nHere is L_3:')
print('  ', L_3)


