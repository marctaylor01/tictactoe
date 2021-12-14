from player import Player
BOARD_SIZE = 3
LAST_CHECK = 2

class Board:
	"""A class representing the board"""
	board = [
			["Empty", "Empty", "Empty"], 
			["Empty", "Empty", "Empty"], 
			["Empty", "Empty", "Empty"]
			]

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
		for row in range(BOARD_SIZE):
			for col in range(BOARD_SIZE):
			# check if empty or other piece
				if (self.board[row][col] != player.playing_piece):
					break
				elif(col == LAST_CHECK):
					return True
		# check each column
		for col in range(BOARD_SIZE):
			for row in range(BOARD_SIZE):
				if (self.board[row][col] != player.playing_piece):
					break
				elif (row == LAST_CHECK):
					return True

		# check the diagonal
		for row_col in range(BOARD_SIZE):
			if (self.board[row_col][row_col] != player.playing_piece):
				break
			elif (row_col == LAST_CHECK):
				return True

		#check outher diagonal (0,2) (1,1) (2,0)
		for row in range(BOARD_SIZE):
			if (self.board[row][BOARD_SIZE-1-row] != player.playing_piece):
				break
			elif (row == LAST_CHECK):
				return True

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
