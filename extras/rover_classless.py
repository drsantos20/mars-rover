"""All the variables are initialised here."""
x_coordinate = 0
y_coordinate = 0
direction = 'N'
left = 'L'
right = 'R'
move = 'M'
north = 'N'
south = 'S'
east = 'E'
west = 'W'
instructions = ''
plat_size = []


def get_input():
	"""This function gets the input from user and sets all the global variables after parsing."""
	global x_coordinate
	global y_coordinate
	global direction
	global instructions
	global plat_size

	plat_size = input().split()
	x_coordinate, y_coordinate, direction = input().split()
	x_coordinate, y_coordinate = int(x_coordinate), int(y_coordinate)
	instructions = input()


def follow_instructions():
	"""This function iterates over each of the instruction and calls the respective command function."""
	global instructions
	for steps in instructions:
		if steps is left:
			turn_left()
		elif steps is right:
			turn_right()
		elif steps is move:
			move_forward()
		else:
			print("Wrong Instruction.")


def move_forward():
	"""Moves the rover based on the present direction the the rover.
	   Assuming that the rover won't move after the plateau edge is reached."""
	global x_coordinate
	global y_coordinate
	global plat_size
	if direction is north and y_coordinate < int(plat_size[1]):
		y_coordinate = y_coordinate + 1
	elif direction is east and x_coordinate < int(plat_size[0]):
		x_coordinate = x_coordinate + 1
	elif direction is south and y_coordinate > 0:
		y_coordinate = y_coordinate - 1
	elif direction is west and x_coordinate > 0:
		x_coordinate = x_coordinate - 1 

def turn_left():
	"""Turns the rover left."""
	global direction

	if direction is north:
		direction = west
	elif direction is east:
		direction = north
	elif direction is south:
		direction = east
	elif direction is west:
		direction = south 

def turn_right():
	"""Turns the rover right."""
	global direction

	if direction is north:
		direction = east
	elif direction is east:
		direction = south
	elif direction is south:
		direction = west
	elif direction is west:
		direction = north 

def print_output():
	"""Prints the final result."""
	print(x_coordinate, y_coordinate, direction)



def main():
	get_input()
	follow_instructions()
	print_output()

if __name__ == '__main__': 
	main()