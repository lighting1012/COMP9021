# Written by *** for COMP9021
import sys
import os
import copy

filename = input('Which data file do you want to use?')
if os.path.exists(filename) == False:
	print('Incorrect input, giving up')
	sys.exit()
L= []
with open (filename) as data_file1:
	n = 0
	for line in data_file1:
		LL = []
		for x in line:
			if x == '\n' or x == ' ':
				continue
			LL.append(int(x)) 
		L.append(LL)
#print('L is:', L)
L1 = list(reversed(L))
L2 = copy.deepcopy(L1)

for i in range(0, len(L)-1):
	for j in range(0, len(L1[i])-1):
		L2[i+1][j] += max(L2[i][j], L2[i][j+1])
y = 0
L3 = L[0]
for x in range(len(L2)-2,-1,-1):
	if L2[x][y] > L2[x][y+1]:
		L3.append(L1[x][y])
	elif L2[x][y] < L2[x][y+1]:
		L3.append(L1[x][y+1])
		y+=1
	else:
		L3.append(L1[x][y])
L4 = copy.deepcopy(L2)
for m in range(0, len(L4)):
	for n in range(0, len(L4[m])):
		L4[m][n] = 1
for x in range(0, len(L2)):
	for y in range(0, len(L2[x])-1):
		if L2[x][y] == L2[x][y+1]:
			L4[x+1][y] = L4[x][y] + L4[x][y+1]

#print('L1 is:', L1)
#print('L2 is:', L2)
#print('L4 is:', L4)
print('The largest sum is:', L2[-1][0])
print('The number of paths yielding this sum is:', L4[-1][0])
print('The leftmost path yielding this sum is:', L3)
# Insert your code here
