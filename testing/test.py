""" import randint from random """
import os
import time


def clear_screen():
    """Clear the terminal after sign in."""
    os.system('clear')


def game_settings():
    """ Set game settings """
    size = game_board_size()
    ships = number_of_ships()
    turns = number_of_turns()


def game_board_size():
    """  verify inputs of the board size 5x5 or 8x8? """
    size = 0
    while size < 5 or size > 8:
        try:
            size = int(input("Choose the number of rows/cols (5-8): "))
            if size < 5 or size > 8:
                print("invalid size. Please choose between 5 or 8?")
        except ValueError:
            print("Please enter a valid number between 5 and 8")
    return size


BOARD_SIZE = game_board_size()
print(f"test {BOARD_SIZE}")

time.sleep(1)
clear_screen()


def number_of_ships():
    """  verify inputs number of ships on the board """
    ships = 0
    while ships < 2 or ships > 6:
        try:
            ships = int(input("How many ships on the board? (2-6): "))
            if ships < 2 or ships > 6:
                print("invalid number of ships! Please choose between 2 or 6?")
        except ValueError:
            print("Please enter a valid number between 2 and 6")
    return ships


SHIPS_ON_THE_BOARD = number_of_ships()
print(f"number of ships {SHIPS_ON_THE_BOARD}")

time.sleep(1)
clear_screen()


def number_of_turns():
    """  verify inputs number of turns to play """
    turns = 0
    while turns < 5 or turns > 10:
        try:
            turns = int(input("How many turns? (5-10): "))
            if turns < 5 or turns > 10:
                print("invalid number of turns! Choose between 5 or 10?")
        except ValueError:
            print("Please enter a valid number between 5 and 10")
    return turns


TURNS_OF_PLAY = number_of_turns()
print(f"number of turns {TURNS_OF_PLAY}")

time.sleep(1)
clear_screen()


def build_board(size):
    """
    Builds the game board and filled with '*'

    Size int the number of rows and columns from user input size.
    """
    return [['*' for _ in range(size)] for _ in range(size)]


def print_board(board):
    for row in range(len(board)):
        print_row = []
        print(" ".join (row))

board = build_board(BOARD_SIZE)
print_board(BOARD_SIZE)