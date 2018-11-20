# Written by *** for COMP9021
import sys
import os
import copy

filename = input('Which data file do you want to use? ')
if os.path.exists(filename) == False:
	print('Incorrect input, giving up')
	sys.exit()
L= []
with open (filename) as data_file:
	for line in data_file:
		LL = []
		for x in line.split(' '):
			if x ==' ' or x == '\n':
				continue
			LL.append(int(x))
		L.append(LL)
#print('L is:', L)
C = []
L1 =[]
for i in range(0, len(L)):
	if L[i] in C:
		continue
	else:
		S = L[i][1]
		M = L[i][1]
		C = [L[i]]
		for j in range(i+1, len(L)):
			S += L[j][1]
			M = min(M, L[j][1])
			if S-(L[j][0]- L[i][0]) >= M *(j-1+1):
				C.append(L[j])
		L1.append(C)
#print('L1 is:',L1)
L2 = []
for i in range(0, len(L1)):
	S = 0
	for j in range(0, len(L1[i])):
		S += L1[i][j][1]
	Q = int((S-(L1[i][-1][0]-L1[i][0][0]))/(len(L1[i])))
	L2.append(Q)
#print('L2 is:', L2)
	
print('The maximum quantity of fish that each town can have is ', min(L2),'.',sep = '')
# Insert your code here
