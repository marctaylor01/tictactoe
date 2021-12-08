import player

class Board:
	"""A class representing the board"""
	board = [
			["Empty", "Empty", "Empty"], 
			["Empty", "Empty", "Empty"], 
			["Empty", "Empty", "Empty"]
			]
	player.Player
	def __init__(self):
		return 

	def is_taken(self, row, column):
		"""Checks if place is taken"""
		return self.board[row][column] != "Empty"

	def reset_board(self):
		"""Resets the board"""
		self.board = [
			["Empty", "Empty", "Empty"], 
			["Empty", "Empty", "Empty"], 
			["Empty", "Empty", "Empty"]
			]

	def check_three_in_a_row(self, player):
		"""Checks if player has won"""
		# check first each row
		for row in range(3):
			for col in range(3):
			# check if empty or other piece
				if (self.board[row][col] != player.playing):
					break
				elif(col == 2):
					return True


		# check each column

		# check the diagonal

	def display(self):
		"""Print out the board"""
		for row in self.board:
			for col in range(3):
				string = row[col]
				if (string == "Empty"):
					string = " " 	
				
				if (col != 2):
					print(string + "|", end="")
				else:
					print(string)
		print("\n")
