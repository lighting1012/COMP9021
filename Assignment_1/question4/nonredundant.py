# Written by *** for COMP9021
import sys
import os
import copy
from collections import defaultdict


filename = input('Which data file do you want to use?')
if os.path.exists(filename) == False:
	print('Incorrect input, giving up')
	sys.exit()

L = []
S = set()
L1 = defaultdict(set)
with open(filename) as datafile:
	for line in datafile:
		L.append([int(line[2]), int(line[4])])
#L is a list which consists of all the direct facts
#print('L is:', L)
for i in range(0,len(L)-1):
	L1[L[i][1]].add(L[i][0])
L2 = copy.deepcopy(L1)
for i in L1.keys():
	for j in L1[i]:
		if j in L1.keys():
			L2[i] = L1[i].union(L1[j])
#L2 now is a dictionary which records all source (includes direct and indirect) of a number
#print('L2 is:', L2)
L3 = copy.deepcopy(L)
for i in range(0, len(L)-1):
	for j in range(i+1, len(L)):
		if L[i][0] == L[j][0]:
			if L[i][1] in L2[L[j][1]]:
				L3[j] = 'redundant'
			elif L[j][1] in L2[L[i][1]]:
				L3[i] = 'redundant'
			else:
				continue
for i in range(len(L3)-1, 1, -1):
	if L3[i] == 'redundant':
		L3.pop(i)
#print('L3 is:', L3)
print('The nonredundant facts are:')
for i in range(0, len(L3)):
	print('R(',L3[i][0],',',L3[i][1],')',sep = '')
# Insert your code here
