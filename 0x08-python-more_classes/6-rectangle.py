#!/usr/bin/python3
"""module to define a class with attributes"""

class Rectangle:
	""" class Rectangle """

	number_of_instances = 0
	"""number of instances counter"""

	def __init__(self, width=0, height=0):
		"""instatiation function"""
		self.width = width
		self.height = height
		Rectangle.number_of_instances += 1
	@property
	def width(self):
		"""private instance attribute width"""
		return self.__width

	@width.setter
	def width(self, value):
		""" function to set the width """
		if type(value) is not int:
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	@property
	def height(self):
		""" private instance height """
		return self.__height

	@height.setter
	def height(self, value):
		""" height function setter"""
		if type(value) is not int:
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value

	def area(self):
		"""area function to return the area"""
		return(self.width * self.height)

	def perimeter(self):
		"""function to return the perimeter"""
		if self.width == 0 or self.height == 0:
			return 0
		else:
			return ((2 * self.width) + (2 * self.height))
	def __str__(self):
        	"""Function that return perimeter of the rectangle"""
        	Rectangleprint = ""
        	if self.height == 0 or self.width == 0:
            		return Rectangleprint
        	for h in range(0, self.height):
            		for w in range(0, self.width):
                		Rectangleprint += "#"
            		Rectangleprint += "\n"
        	return Rectangleprint[:-1]

	def __repr__(self):
        	""" return a string representation of the rectangle"""
        	return ("Rectangle({:d}, {:d})".format(self.width, self.height))

	def __del__(self):
		"""prints an error message when an instance is deleted"""
		print("Bye rectangle...")
		Rectangle.number_of_instances -= 1

