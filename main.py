import random

board = [
		[" |", " |", " "],
		[" |", " |", " "],
		[" |", " |", " "]]

p1 = "X"
p2 = "O"

def display_board():
	for row in board:
		print(row[0], row[1], row[2])
	
	print("\n")

def place_piece(row, column, piece):
	"place piece in a specific row and column"
	if is_taken(row, column):
		print("Can not put piece there. Please try again!")
		#ask for row, column again
	elif column == 2:
		board[row][column] = f"{piece}"
	else:
		board[row][column] = f"{piece}|"


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


def switch_turn(cur_user):
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
	return row, column


def main():
	"""Loops through game and"""
	turn = None
	display_board()
	turn = get_player_turn(turn)
	for i in range(9):
		while(True):	
			row, column = ask_place()
			if (not is_taken(row, column)):
				break
			
		place_piece(row, column, turn)
		turn = switch_turn(turn)

		display_board()


main()
"""
if __name__== "__main__":
	turn = get_player_turn(turn)
	place_piece(0, 0, 'X')
	display_board()
	place_piece(0, 0, "O")
	main()
	"""

		