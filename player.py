class Player:
	"""Representing a player in tic tac toe"""

	def __init__(self, playing_piece) -> None:
		self.playing_piece = playing_piece


	def place_piece(self, row, column, board):
		"place piece in a specific row and column"
		if board.is_taken(row, column):
			print("Can not put piece there. Please try again!")
		else:
			board.place_piece(row, column, self)