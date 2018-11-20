# Defines two classes, Point() and Triangle().
# An object for the second class is created by passing named arguments,
# point_1, point_2 and point_3, to its constructor.
# Such an object can be modified by changing one point, two or three points
# thanks to the method change_point_or_points().
# At any stage, the object maintains correct values
# for perimeter and area.
#
# Written by *** and Eric Martin for COMP9021


from math import sqrt


class PointError(Exception):
	def __init__(self, message):
		self.message = message


class Point():
	def __init__(self, x = None, y = None):
		if x is None and y is None:
			self.x = 0
			self.y = 0
		elif x is None or y is None:
			raise PointError('Need two coordinates, point not created.')
		else:
			self.x = x
			self.y = y
            
    # Possibly define other methods


class TriangleError(Exception):
	def __init__(self, message):
		self.message = message


class Triangle:
	def __init__(self, *, point_1, point_2, point_3):
		self.point_1 = point_1
		self.point_2 = point_2
		self.point_3 = point_3
		if (point_1.x - point_2.x) * (point_1.y - point_3.y) == (point_1.y - point_2.y) * (point_1.x - point_3.x):
			raise TriangleError('Incorrect input, triangle not created.')
		a = sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)
		b = sqrt((point_1.x - point_3.x) ** 2 + (point_1.y - point_3.y) ** 2)
		c = sqrt((point_3.x - point_2.x) ** 2 + (point_3.y - point_2.y) ** 2)
		self.perimeter = a + b + c
		p = self.perimeter / 2
		self.area = sqrt(p * (p - a) * (p - b) * (p - c))
	def change_point_or_points(self, *, point_1 = None,point_2 = None, point_3 = None):
		if point_1 is not None:
			self.point_1 = point_1
		if point_2 is not None:
			self.point_2 = point_2
		if point_3 is not None:
			self.point_3 = point_3
		
		
		if (self.point_1.x - self.point_2.x) * (self.point_1.y - self.point_3.y) == (self.point_1.y - self.point_2.y) * (self.point_1.x - self.point_3.x):
			print('Incorrect input, triangle not modified.')
		else:
			self.a = sqrt((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2)
			self.b = sqrt((self.point_1.x - self.point_3.x) ** 2 + (self.point_1.y - self.point_3.y) ** 2)
			self.c = sqrt((self.point_3.x - self.point_2.x) ** 2 + (self.point_3.y - self.point_2.y) ** 2)
			self.perimeter = self.a + self.b + self.c
			self.p = self.perimeter / 2
			self.area = sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
    # Possibly define other methods
	
            
