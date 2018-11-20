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
	for line in data_file1:
		x1, y1, x2, y2 = line.split(' ')
		x1 = int(x1)
		x2 = int(x2)
		y1 = int(y1)
		y2 = int(y2)
		L.append([(x1,y1),(x2,y1),(x1,y2),(x2,y2)])
#print('L is:', L)

def inside(P, R):
	if P[0] >= R[0][0] and\
	P[0] <=R[-1][0] and\
	P[1] >= R[0][1]and\
	P[1] <= R[-1][1]:
		return(True)
	else:
		return(False)
	
count = 0
result = 0
for i in range(0, len(L)):
	R = L[i]
	LB = R[0]
	RB = R[1]
	LU = R[2]
	RU = R[3]
	for k in range(LB[1], LU[1]):
		count = 1
		for j in range(0, len(L)):
			if j == i:
				continue
			else:
				if inside((LB[0],k), L[j]) == True and inside((LB[0],k+1),L[j]) == True:
					count = 0
					break
		result += count
	for k in range(LB[1], LU[1]):
		count = 1
		for j in range(0, len(L)):
			if j == i:
				continue
			else:
				if inside((RB[0],k), L[j]) == True and inside((RB[0],k+1),L[j]) == True:
					count = 0
					break
		result += count
	for k in range(LB[0], RB[0]):
		count = 1
		for j in range(0, len(L)):
			if j == i:
				continue
			else:
				if inside((k,LB[1]), L[j]) == True and inside((k+1,LB[1]),L[j]) == True:
					count = 0
					break
		result += count
	for k in range(LB[0], RB[0]):
		count = 1
		for j in range(0, len(L)):
			if j == i:
				continue
			else:
				if inside((k,LU[1]), L[j]) == True and inside((k+1,LU[1]),L[j]) == True:
					count = 0
					break
		result += count
print('The perimeter is:', result)
	
	
	
	
# Insert your code here
