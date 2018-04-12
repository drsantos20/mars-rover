directions = 'NESW' # All the probable directions
direction_shift = [(0,1),(1,0),(0,-1),(-1,0)] # All the possible shift scenarios for each direction.


# Lambda functions for each of the given instructions.
turn_left = lambda x_coord, y_coord, position: (x_coord, y_coord, (position + 1) % 4)
turn_right = lambda x_coord, y_coord, position: (x_coord, y_coord, (position - 1 + 4) % 4)
move_forward = lambda x_coord, y_coord, position: (x_coord+direction_shift[position][0], y_coord+direction_shift[position][1], position)




plat_size = input().split() # This variable is actually not used and ignored in this program.
x_coord, y_coord, direction = input().split() # Initial status of rover.
rover_status = int(x_coord), int(y_coord), directions.find(direction)
instructions = input().upper() # Instructions to be executed.

# each instruction is executed and corresponding lambda function is called.
for steps in instructions:
	if steps is 'L':
		rover_status = turn_left(rover_status[0], rover_status[1], rover_status[2])
	elif steps is 'R':
		rover_status = turn_right(rover_status[0], rover_status[1], rover_status[2])
	elif steps is 'M':
		rover_status = move_forward(rover_status[0], rover_status[1], rover_status[2])
	else:
		print("Wrong Instruction.")

# Printing the result back.
print(rover_status[0], rover_status[1], directions[rover_status[2]])

