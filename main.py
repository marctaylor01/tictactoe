import random
from board import *
from player import Player

class TicTacToe:
	"""A class representing the game"""


def switch_turn(cur_player, player1, player2):
	"""Switch the users turns"""
	if cur_player == player1:
		return player2
	else:
		return player1


def ask_place():
	"""Ask user to put in row and column, returns as a tuple."""
	print("Which row would you like to put it in?")
	try:
		row = int(input())
		print("Which column would you like to put it in?")
		column = int(input())
		assert (0 < row < 4 and  0 < column < 4) 
		return row-1, column-1
	except:
		print("Your row or column is not a valid place on the board")
		return ask_place()


def reset_game(board) :
	"""Shall clear the terminal and prepare for next game"""
	# clear the board
	board.reset_board()
	board.display()

# 
def main():
	"""Loops through game and prints and has the structure for a simple
		game of tic tac toe."""
	# init game components
	board = Board(3, 3)
	player_one = Player("X")
	player_two = Player("O")

	board.display()

	# check 
	continue_playing = True
	current_player = random.choice([player_one, player_two])
	while (continue_playing):
		print(str(current_player.playing_piece) + " turn")

		# gets a valid place to put piece
		row, col = ask_place()
		while (board.is_taken(row, col)):
			print("Is already taken, try another place!")
			row, col = ask_place()
		current_player.place_piece(row, col, board)
		
		board.display()
		# check if game is over
		if (board.has_won(current_player)):
			print(str(current_player.playing_piece) + " has won")
			play_again = None
			print("Would you like to play again? y/n!")
			while (play_again != "y" and play_again != "n") :
				play_again = input()
			if (play_again == "y") :
				reset_game(board)
			else :
				continue_playing = False
		# in case of draw
		elif (board.is_full()) :
			print("It is a tie, would you like to play again? y/n!")
			play_again = None
			while (play_again != "y" and play_again != "n") :
				play_again = input()
			if (play_again == "y") :
				reset_game(board)
				pass
			else :
				continue_playing = False

		current_player = switch_turn(current_player, player_one, player_two)

def four_in_a_row():
	"""Play a game of 4 in a row"""
	player1 = Player("X")
	player2 = Player("O")
	board = FourInARowBoard(6, 7)
	board.display()

	playing = True
	current_player = random.choice([player1, player2])
	while (playing):
		print(str(current_player.playing_piece) + " turn.")
		column = 0
		while(True):
			try:
				column = int(input())
			except:
				pass
			if (0 < column <= board.COLUMNS):
				if (board.is_valid(column-1)):
					break
				else:
					print("Can not put piece there! Please insert another column.")
			else:
				print("Input was not valid, needs to be in bounds! Try again.")


		x, y = board.place_piece(column-1, current_player)
		board.display()
		# check if won
		# if won congratulate and break
		if (board.has_won(current_player, x, y)):
			print(f"Congratulations! {current_player} has won the game!!!")
			break
		# else continue
		current_player = switch_turn(current_player, player1, player2)


four_in_a_row()
# main()