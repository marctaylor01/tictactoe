import random
from board import Board
from player import Player

board = [
		[" ", " ", " "],
		[" ", " ", " "],
		[" ", " ", " "]]


def display_board():
	for row in board:
		print(row[0] + "|", row[1] + "|", row[2])
	print("\n")

def place_piece(row, column, piece):
	"place piece in a specific row and column"
	if is_taken(row, column):
		print("Can not put piece there. Please try again!")
		#ask for row, column again
	else:
		board[row][column] = piece


def is_taken(row, column):
	"""Checks if piece is already put on specific spot"""
	if p1 in board[row][column] or p2 in board[row][column]:
		return True
	return False


def get_player_turn(turn):
	"""Switch players turn and randomize starter"""
	if turn == None:
		# randomize player
		number = random.randint(1,2)
		if number == 1:
			turn = p1
		else:
			turn = p2
	return turn


def switch_turn(cur_user, ):
	"""Switch the users turns"""
	if cur_user == p1:
		return p2
	else:
		return p1


def ask_place():
	"""Ask user to put in row and column, returns as a tuple."""
	print("Which row would you like to put it in?")
	row = int(input())
	print("Which column would you like to put it in?")
	column = int(input())
	return row-1, column-1


def get_piece(row, column):
	"""Returns piece of row and column on board"""
	return board[row][column]


def	has_won(piece, row, column):
	"""Checks if the player won when placing its latest piece""" 
	# We will need to know what piece we are looking for
	# We will then need to know the row and column placement
	# first check column if three in a row
	for i in range(3):
		# check if wrong piece then break
		if (piece == get_piece(i, column)):
			if (i == 2):
				return True
		else:
			break
	return False
	# second check row if three in a row2

	# last check diagonal
	
	# return true statement if player has won
	# else return false


def main():
	"""Loops through game and"""
	board = Board()
	player_one = Player("X")
	player_two = Player("O")
	board.display()

	continuePlaying = True
	currentPlayer = random.choice([player_one, player_two])
	while (continuePlaying):
		currentPlayer.place_piece(0, 0, board)
		break
		pass
	board.display()
	"""turn = None
	for i in range(3):
		print(i)
	display_board()
	turn = get_player_turn(turn)
	print(f"Player with {turn} starts!")
	for i in range(9):
		while(True):	
			row, column = ask_place()
			if (not is_taken(row, column)):
				break
			print("Place is taken, try again")
		place_piece(row, column, turn)
		display_board()
		# check if piece won the game
		if (has_won(turn, row, column)):
			print(f"Player {turn} has won, congratulations!")
			# break or restart
		turn = switch_turn(turn)"""
		


main()
"""
if __name__== "__main__":
	turn = get_player_turn(turn)
	place_piece(0, 0, 'X')
	display_board()
	place_piece(0, 0, "O")
	main()
	"""

		