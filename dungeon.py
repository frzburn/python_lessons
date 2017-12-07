import random



	

# Draw grid

# Pick a random location for player

# Pick a random location for exit door

# Pick random location for monster

# Draw player in the grid

# Take input for movement

# Move player, unless invalid move

# Check for win/lose


class Game:
	''' Grid '''
	class Grid:
		CELLS = []
		
		''' Create the grid '''
		def __init__(self):
			self.CELLS = [(x, y) for y in range(5) for x in range(5)]
			
		# Clear screen and redraw grid
		def draw_grid():
			
			
		
	class GameObject:
		position = []
		
		
		def __init__(self):
			
			
		def get_position():
			return self.position
		
		
	''' Player '''
	class Player(GameObject):
		move_history = []
	
	
		def move(dir):
			# Get player location
			
			# Get valid moves
			
			# Change the player location
			
			# Redraw grid
			
			
			

		# Returns a list of valid moves from the player position
		def get_moves():
			moves = ["LEFT", "RIGHT", "UP", "DOWN"]
			
			# Check valid moves
			if get_position(self)[0] == 0:
				del moves["LEFT"]
			
			if get_position(self)[0] == 4:
				del moves["RIGHT"]
			if get_position(self)[1] == 0:
				del moves["UP"]
			if get_position(self)[1] == 4:
				del moves["DOWN"]	
			
			return moves
	
	
	







def game():
	# Create the grid
	grid = Grid()
	
	
	
	

def main():
	print('''
	Welcome to the Dungeon!
	You are currently in room {}
	You can move {}
	
	Enter QUIT to quit
	''')
	
	# Start game
	game()

	
main()
