""" 

INPUT AND OUTPUT

Test Input:
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
 
Expected Output:
1 3 N
5 1 E

"""
class rover:
	def __init__(self):
		"""All the variables are initialised here."""
		self.x = 0 
		self.y = 0
		self.direction = 'N'
		self.left = 'L'
		self.right = 'R'
		self.move = 'M'
		self.north = 'N'
		self.south = 'S'
		self.east = 'E'
		self.west = 'W'
		self.coordinates = ''
		self.plateau_size = []

	def set_data(self, plateau_size, x, y, direction, coordinates):
		"""This function gets the input from main and sets all the variables of class."""
		self.plateau_size = plateau_size 
		self.x, self.y, self.direction = x, y, direction
		self.coordinates = coordinates



	def coordinates_follow(self):
		"""This function iterates over each of the instruction and calls the respective command function."""
		for steps in self.coordinates:
			if steps is self.left:
				self.turn_left()
			elif steps is self.right:
				self.turn_right()
			elif steps is self.move:
				self.move_forward()
			else:
				print("Wrong Instruction.")

	
	def move_forward(self):
		"""Moves the rover based on the present direction the the rover.
		   Assuming that the rover won't move after the plateau edge is reached."""
		if self.direction == self.north and self.y < int(self.plateau_size[1]):
			self.y = self.y + 1
		elif self.direction == self.east and self.x < int(self.plateau_size[0]):
			self.x = self.x + 1
		elif self.direction == self.south and self.y > 0:
			self.y = self.y - 1
		elif self.direction == self.west and self.x > 0:
			self.x = self.x - 1 

	
	def turn_left(self):
		"""Turns the rover left."""
		if self.direction == self.north:
			self.direction = self.west
		elif self.direction == self.east:
			self.direction = self.north
		elif self.direction == self.south:
			self.direction = self.east
		elif self.direction == self.west:
			self.direction = self.south 

	
	def turn_right(self):
		"""Turns the rover right."""
		if self.direction == self.north:
			self.direction = self.east
		elif self.direction == self.east:
			self.direction = self.south
		elif self.direction == self.south:
			self.direction = self.west
		elif self.direction == self.west:
			self.direction = self.north 

	
	def get_result(self):
		"""Returns the final result."""
		return self.x, self.y, self.direction



def main():
	r = rover()
	plateau_size = input().split()
	x, y, direction = input().split()
	coordinates = input()
	r.set_data(plateau_size, int(x), int(y), direction.upper(), coordinates.upper())
	r.coordinates_follow()
	result = r.get_result()
	print(result[0], result[1], result[2])

if __name__ == '__main__': 
	main()
