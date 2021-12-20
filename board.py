from player import Player
BOARD_SIZE = 3
LAST_CHECK = 2

class Board:
	"""A class representing the board, shall be able to represent any size board"""
	board = []

	def __init__(self, rows, columns):
		self.ROWS = rows
		self.COLUMNS = columns
		# Diagonal for any board
		if (rows < columns):
			self.DIAGONAL = rows
		else:
			self.DIAGONAL = columns

		for i in range(rows):
			self.board.append([])
			for j in range(columns):
				self.board[i].append("Empty")
		return 

	def is_taken(self, row, column):
		"""Checks if place is taken"""
		return self.board[row][column] != "Empty"

	def reset_board(self):
		"""Resets the board"""
		for row in range(self.ROWS):
			for col in range(self.COLUMNS):
				self.board[row][col] = "Empty"
	

	def is_full(self):
		"""Checks if the board is filled with pieces"""
		for row in self.board :
			for col in row :
				if (col == "Empty") :
					return False
		return True


	def has_won(self, player):
		"""Checks if player has won"""
		# check first each row
		for row in range(self.ROWS):
			for col in range(self.COLUMNS):
			# check if empty or other piece
				if (self.board[row][col] != player.playing_piece):
					break
				elif(col == LAST_CHECK):
					return True
		# check each column
		for col in range(self.ROWS):
			for row in range(self.COLUMNS):
				if (self.board[row][col] != player.playing_piece):
					break
				elif (row == LAST_CHECK):
					return True

		# check the diagonal
		for row_col in range(self.ROWS):
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
			for place in range(len(row)):
				string = row[place]
				if (string == "Empty"):
					string = " " 	
				
				if (place != len(row)-1):
					print(string + "|", end="")
				else:
					print(string)
		print("\n")


	def place_piece(self, row, col, player):
		"""Place a piece in the board depending on row and column"""
		self.board[row][col] = player.playing_piece


class FourInARowBoard(Board):
	"""
		Board representation for a game of four in a row. Has similar
		functions but will override some of the functions for correct
		implemntation of game.
	"""
	def __init__(self, rows, columns):
		super().__init__(rows, columns)
	
	
	def is_valid(self, column):
		"""
			Check only if the top in that column is empty to see if a placement
			will be possible.
		"""
		return self.board[0][column] == "Empty"

	# might for performance purpose override is_full function


	def place_piece(self, row, col, player):
		"""Place pice in certain column, row is not necessary only for practical reasons
			Does the calculations of dropping the piece"""
		find_row = self.ROWS - 1
		while(self.is_taken(find_row, col)):
			find_row -= 1

		self.board[find_row][col] = player.playing_piece
	

	def has_won(self, player, row, col):
		"""Check if the player who played has won"""
		# Counter
		in_a_row = 0
		
		# Check row first
		for piece in self.board[row]:
			if (piece == player.playing_piece):
				in_a_row += 1
			else:
				in_a_row = 0
			if (in_a_row == 4):
				return True

		# Check column
		for i in range(self.ROWS):
			if (self.board[i][col] == player.playing_piece):
				in_a_row += 1
			else:
				in_a_row = 0
			if (in_a_row == 4):
				return True

		# go through each diagonal, first left diagonal
		# assume we have put it into row and col
		start_x, start_y = col, row
		while(start_x != 0 or start_y != 0):
			start_y -= 1
			start_x -= 1
		while(True):
			try:
				if (self.board[start_y][start_x] == player.playing_piece):
					in_a_row += 1
				else:
					in_a_row = 0
				if (in_a_row == 4):
					return True
				start_x += 1
				start_y += 1
			except:
				break


		start_x, start_y = col, row
		while (start_x != self.board.COLUMNS - 1 or start_y != 0):
			start_y -=1
			start_x +=1

		while(True):
			try:
				if (self.board[start_y][start_x] == player.playing_piece):
					in_a_row += 1
				else:
					in_a_row = 0
				if (in_a_row == 4):
					return True
				start_x -= 1
				start_y += 1
			except:
				break


