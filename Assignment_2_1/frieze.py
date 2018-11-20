# Insert your code here
# written by Jiaquan Xu
import os

class FriezeError(Exception):
	def __init__(self, message):
		self.message = message

class FileNotFoundError(Exception):
	def __init__(self, message):
		self.message = message

class Frieze():
	def __init__(self, filename):
		self.file = filename
		if os.path.exists(self.file) == False:
			raise FileNotFoundError('File Not Found')
		with open(self.file) as datafile:
			self.L = []
			for line in datafile:
				LL = []
				for s in line.split(' '):
					if s == '\n' or s == '':
						continue
					else:
						if s.isdigit() == False and s[-1:] != '\n':
							raise FriezeError('Incorrect input.')
						else:
							if int(s) >= 0 and int(s) <= 15:
								LL.append(int(s))
							else:
								raise FriezeError('Incorrect input.')
				if len(LL):
					self.L.append(LL)
		if len(self.L) < 3 or len(self.L) > 17 or len(self.L[0]) < 5 or len(self.L[0]) > 51 :
			raise FriezeError('Incorrect input.')
		for i in range(len(self.L)-1):
			if len(self.L[i]) != len(self.L[i+1]):
				raise FriezeError('Incorrect input.')
			
		L = self.L
		for i in range(len(L)):
			if L[i][-1] == 1 and L[i][0] in [0,2,4,6,8,10,12,14]:
				raise FriezeError('Input does not represent a frieze.')
			if L[i][-1] == 0 and L[i][0] in [1,3,5,7,9,11,13,15]:
				raise FriezeError('Input does not represent a frieze.')
			if L[i][-1] != 0 and L[i][-1] != 1:
				raise FriezeError('Input does not represent a frieze.')
		for j in range(len(L[0])-1):
			if L[0][j] not in [4,12] or L[-1][j] not in [4,5,6,7]:
				raise FriezeError('Input does not represent a frieze.')
			for i in range(len(L)-1):
				if L[i][j] in [8,9,10,11,12,13,14,15] and L[i+1][j] in [2,3,6,7,10,11,14,15]:
					raise FriezeError('Input does not represent a frieze.')
		possibleperiod = []
		for i in range(2,len(L[0])//2+1):
			if (len(L[0])-1) % i == 0:
				possibleperiod.append(i)
		if possibleperiod == []:
			raise FriezeError('Input does not represent a frieze.')
		if all(L[i][j] == L[i][j+1] for i in range(len(L)) for j in range(len(L[0])-2)):
			raise FriezeError('Input does not represent a frieze.')
		this_period = False
		for k in possibleperiod:
			if all(L[i][j] == L[i][j+k] for i in range(len(L)) for j in range(len(L[0])-k-1)):
				this_period = True
				period = k
				break
		if this_period == False:
			raise FriezeError('Input does not represent a frieze.')
		else:
			self.period = period	
			
	def display(self):
		new_file = self.file[:-4] + '.tex'
		with open(new_file, 'w') as output_file:
			print(r'''\documentclass[10pt]{article}
\usepackage{tikz}
\usepackage[margin=0cm]{geometry}
\pagestyle{empty}

\begin{document}

\vspace*{\fill}
\begin{center}
\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]''', file = output_file)	
			print(r'''% North to South lines''', file = output_file)
			L = self.L
			for j in range(len(L[0])):
				L1 = []
				for i in range(1, len(L)):
					if  L[i][j] % 2 == 1:
						L1.append(i-1)
						L1.append(i)
				if not L1:
					continue
				elif len(L1) < 3:
					print(f'    \draw ({j},{L1[0]}) -- ({j},{L1[1]});', file = output_file)
				else:
					L2 = [L1[0]]
					for k in range(1, len(L1)-1):
						if L1[k] == L1[k-1] or L1[k] == L1[k+1]:
							continue
						else:
							L2.append(L1[k])
					L2.append(L1[-1])
					for k in range(0,len(L2),2):
						print(f'    \draw ({j},{L2[k]}) -- ({j},{L2[k+1]});', file = output_file)
			print(r'''% North-West to South-East lines''', file = output_file)
			S1 = set()
			for i in range(len(L)-1):
				for j in range(len(L[0])-1):
					if (i,j) in S1:
						continue
					if L[i][j] in [8,9,10,11,12,13,14,15]:
						S1.add((i,j))
						k = 0
						while L[i+k][j+k] in [8,9,10,11,12,13,14,15]:
							k += 1
							S1.add((i+k,j+k))
						print(f'    \draw ({j},{i}) -- ({j+k},{i+k});', file = output_file)			
			print(r'''% West to East lines''', file = output_file)			
			for i in range(len(L)):
				L1 = []
				for j in range(0, len(L[0])-1):
					if  L[i][j] in [4,5,6,7,12,13,14,15]:
						L1.append(j)
						L1.append(j+1)
				if not L1:
					continue
				elif len(L1) < 3:
					print(f'    \draw ({L1[0]},{i}) -- ({L1[1]},{i});', file = output_file)
				else:
					L2 = [L1[0]]
					for k in range(1, len(L1)-1):
						if L1[k] == L1[k-1] or L1[k] == L1[k+1]:
							continue
						else:
							L2.append(L1[k])
					L2.append(L1[-1])
					for k in range(0,len(L2),2):
						print(f'    \draw ({L2[k]},{i}) -- ({L2[k+1]},{i});', file = output_file)
			print(r'''% South-West to North-East lines''', file = output_file)
			S1 = set()
			L2 = []
			for i in range(len(L)-1,0,-1):
				for j in range(len(L[0])-2,-1,-1):
					if (i,j) in S1:
						continue
					if L[i][j] in [2,3,6,7,10,11,14,15]:
						S1.add((i,j))
						k = 0
						while L[i-k][j+k] in [2,3,6,7,10,11,14,15]:
							k += 1
							S1.add((i-k,j+k))
						L2.append((j,i))
						L2.append((j+k,i-k))
			for t in range(len(L2)-1,-1,-2):
				print(f'    \draw ({L2[t-1][0]},{L2[t-1][1]}) -- ({L2[t][0]},{L2[t][1]});', file = output_file)
			print(r'''\end{tikzpicture}
\end{center}
\vspace*{\fill}

\end{document}''', file = output_file)	
			
			
	def analyse(self):
		period = self.period
		if self.horizontal_reflection_check() == False and self.glided_horizontal_reflection_check() == False and self.verticle_reflection_check() == False and self.rotation_check() == False:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation only.')
		if self.horizontal_reflection_check() == True and self.glided_horizontal_reflection_check() == False and self.verticle_reflection_check() == False and self.rotation_check() == False:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
			print('        and horizontal reflection only.')
		if self.horizontal_reflection_check() == False and self.glided_horizontal_reflection_check() == True and self.verticle_reflection_check() == False and self.rotation_check() == False:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
			print('        and glided horizontal reflection only.')
		if self.horizontal_reflection_check() == False and self.glided_horizontal_reflection_check() == False and self.verticle_reflection_check() == True and self.rotation_check() == False:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
			print('        and vertical reflection only.')
		if self.horizontal_reflection_check() == False and self.glided_horizontal_reflection_check() == False and self.verticle_reflection_check() == False and self.rotation_check() == True:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
			print('        and rotation only.')
		if self.horizontal_reflection_check() == False and self.glided_horizontal_reflection_check() == True and self.verticle_reflection_check() == True and self.rotation_check() == True:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation,')
			print('        glided horizontal and vertical reflections, and rotation only.')
		if self.horizontal_reflection_check() == True and self.glided_horizontal_reflection_check() == False and self.verticle_reflection_check() == True and self.rotation_check() == True:
			print(f'Pattern is a frieze of period {self.period} that is invariant under translation,')
			print('        horizontal and vertical reflections, and rotation only.')
	def horizontal_reflection_check(self):
		## horizontal_reflection
		L = self.L
		period = self.period
		horizontal_reflection = True
		for i in range(1, len(L)//2 + 1):
			for j in range(period):
				if L[i][j]%2 != L[len(L)-i][j]%2:
					horizontal_reflection = False
					break
				if L[i][j] in [4,5,6,7,12,13,14,15] and L[len(L)-1-i][j] not in [4,5,6,7,12,13,14,15]:
					horizontal_reflection = False
					break
				if L[i][j] not in [4,5,6,7,12,13,14,15] and L[len(L)-1-i][j] in [4,5,6,7,12,13,14,15]:
					horizontal_reflection = False
					break				
				if L[i][j] in [2,3,6,7,10,11,14,15] and L[len(L)-1-i][j] not in [8,9,10,11,12,13,14,15]:
					horizontal_reflection = False
					break
				if L[i][j] not in [2,3,6,7,10,11,14,15] and L[len(L)-1-i][j] in [8,9,10,11,12,13,14,15]:
					horizontal_reflection = False
					break				
				if L[i-1][j] in [8,9,10,11,12,13,14,15] and L[len(L)-i][j] not in [2,3,6,7,10,11,14,15]:
					horizontal_reflection = False
					break
				if L[i-1][j] not in [8,9,10,11,12,13,14,15] and L[len(L)-i][j] in [2,3,6,7,10,11,14,15]:
					horizontal_reflection = False
					break
			if horizontal_reflection == False:
				break

		if horizontal_reflection == True:
			return True
		else:
			return False
	
	def glided_horizontal_reflection_check(self):
		## glided_horizontal_reflection
		L = self.L
		period = self.period
		if period % 2 != 0:
			return False
		glided_horizontal_reflection = True
		for i in range(1, len(L)//2 + 1):
			for j in range(period):
				if L[i][j]%2 != L[len(L)-i][j+period//2]%2:
					horizontal_reflection = False
					break
				if L[i][j] in [4,5,6,7,12,13,14,15] and L[len(L)-1-i][j+period//2] not in [4,5,6,7,12,13,14,15]:
					horizontal_reflection = False
					break
				if L[i][j] not in [4,5,6,7,12,13,14,15] and L[len(L)-1-i][j+period//2] in [4,5,6,7,12,13,14,15]:
					horizontal_reflection = False
					break				
				if L[i][j] in [2,3,6,7,10,11,14,15] and L[len(L)-1-i][j+period//2] not in [8,9,10,11,12,13,14,15]:
					horizontal_reflection = False
					break
				if L[i][j] not in [2,3,6,7,10,11,14,15] and L[len(L)-1-i][j+period//2] in [8,9,10,11,12,13,14,15]:
					horizontal_reflection = False
					break				
				if L[i-1][j] in [8,9,10,11,12,13,14,15] and L[len(L)-i][j+period//2] not in [2,3,6,7,10,11,14,15]:
					horizontal_reflection = False
					break
				if L[i-1][j] not in [8,9,10,11,12,13,14,15] and L[len(L)-i][j+period//2] in [2,3,6,7,10,11,14,15]:
					horizontal_reflection = False
					break	
			if glided_horizontal_reflection == False:
				break

		if glided_horizontal_reflection == True:
			return True
		else:
			return False				

	def verticle_reflection_check(self):
		L = self.L
		period = self.period
		k = period*0.5
		verticle_reflection = True
		while k <= period:
			axis = k
			verticle_reflection = True
			for i in range(1,len(L)):
				for j in range(1, int(axis)+1):
					if L[i][j] %2 != L[i][int(2*axis)-j] %2:
						verticle_reflection = False
						break
					if L[i][j-1] %2 != L[i][int(2*axis)-j+1] %2:
						verticle_reflection = False
						break
					if L[i][j-1] in [4,5,6,7,12,13,14,15] and L[i][int(2*axis)-j] in [0,1,2,3,8,9,10,11]:
						verticle_reflection = False
						break
					if L[i][j-1] not in [4,5,6,7,12,13,14,15] and L[i][int(2*axis)-j] not in [0,1,2,3,8,9,10,11]:
						verticle_reflection = False
						break
					if L[i][j-1] in [2,3,6,7,10,11,14,15] and L[i-1][int(2*axis)-j] in [0,1,2,3,4,5,6,7]:
						verticle_reflection = False
						break
					if L[i][j-1] not in [2,3,6,7,10,11,14,15] and L[i-1][int(2*axis)-j] not in [0,1,2,3,4,5,6,7]:
						verticle_reflection = False
						break					
					if L[i-1][j-1] in [8,9,10,11,12,13,14,15] and L[i][int(2*axis)-j] in [0,1,4,5,8,9,12,13]:
						verticle_reflection = False
						break
					if L[i-1][j-1] not in [8,9,10,11,12,13,14,15] and L[i][int(2*axis)-j] not in [0,1,4,5,8,9,12,13]:
						verticle_reflection = False
						break					
				if verticle_reflection == False:
					break
			if verticle_reflection == True:
				break
			else:
				k = k+0.5
		if verticle_reflection == True:
			return True
		else:
			return False
		
	def rotation_check(self):
		L = self.L
		period = self.period
		k = period*0.5
		rotation = True
		while k <= period:
			axis = k
			rotation = True
			for i in range(1,len(L)//2+1):
				for j in range(1, int(axis)+1):
					if L[i][j-1] %2 != L[len(L)-1-i+1][int(2*axis)-j+1] %2:
						rotation = False
						break
					if L[i][j-1] in [2,3,6,7,10,11,14,15] and L[len(L)-1-i+1][int(2*axis)-j] in [0,1,4,5,8,9,12,13]:
						rotation = False
						break
					if L[i][j-1] not in [2,3,6,7,10,11,14,15] and L[len(L)-1-i+1][int(2*axis)-j] not in [0,1,4,5,8,9,12,13]:
						rotation = False
						break					
					if L[i][j-1] in [4,5,6,7,12,13,14,15] and L[len(L)-1-i][int(2*axis)-j] in [0,1,2,3,8,9,10,11]:
						rotation = False
						break
					if L[i][j-1] not in [4,5,6,7,12,13,14,15] and L[len(L)-1-i][int(2*axis)-j] not in [0,1,2,3,8,9,10,11]:
						rotation = False
						break					
					if L[i-1][j-1] in [8,9,10,11,12,13,14,15] and L[len(L)-1-i][int(2*axis)-j] in [0,1,2,3,4,5,6,7]:
						rotation = False
						break
					if L[i-1][j-1] not in [8,9,10,11,12,13,14,15] and L[len(L)-1-i][int(2*axis)-j] not in [0,1,2,3,4,5,6,7]:
						rotation = False
						break					
					if L[i][j] %2 != L[len(L)-1-i+1][int(2*axis)-j] %2:
						rotation = False
						break
				if rotation == False:
					break
			if rotation == True:
				break
			else:
				k = k+0.5
		if rotation == True:
			return True
		else:
			return False
		
