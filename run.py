""" The retry of a new version of battleship game. """
from random import randint
import os
import time


def clear_screen():
    """Clear the terminal after sign in."""
    os.system('clear')


def logo():
    """Welcome game logo"""
    print(r"""
   ___       __  __  __        __   _
  / _ )___ _/ /_/ /_/ ___ ___ / /  (____
 / _  / _ `/ __/ __/ / -_(_-</ _ \/ / _ \
/____/\_,_/\__/\__/_/\__/___/_//_/_/ .__/
                                  /_/
""")


def welcome():
    """Welcome greeting"""
    print("Ahoy, sailor! to my simple version of battleship!\n")
    print("           Ready to conquer the seas?\n")


#  calling the logo first and the greeting text.
logo()
welcome()


name = input("Please enter your name: ")
"""username input while loop"""
while not name:
    print("Every sailor has a name? try again!")
    name = input("Please enter your name: ")
else:
    print(f"\nWelcome aboard Sailor {name}! Ready to sink some ships!")


time.sleep(2)
clear_screen()


def game_settings():
    """ Set game settings """
    size = game_board_size()
    ships = number_of_ships()
    turns = number_of_turns()
    return size


def game_board_size():
    """  verify inputs of the board size 5x5 or 8x8? """
    size = 0
    while size != 5 and size != 8:
        try:
            size = int(input("Choose the number of rows/cols (5-8): "))
            if size != 5 and size != 8:
                print("invalid size. Please choose between 5 or 8?")
        except ValueError:
            print("Please enter a valid number between 5 and 8")
    return size


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


def build_board(size):
    """
    Builds the game board and filled with '*'

    Size int the number of rows and columns from user input size.
    """
    return [['*' for _ in range(size)] for _ in range(size)]


def print_board(board):
    """ Display the game board in the terminal """
    for i, row in enumerate(board):
        print_row = []
        for j, cell in enumerate(row):
            if cell == 'S':
                print_row.append('*')
            else:
                print_row.append(cell)
        print(" ".join(print_row))


def main():
    """ Validate and check the value input to build the board 5x5 or 8x8 """
    board_size = game_board_size()
    board = build_board(board_size)

    time.sleep(1)
    clear_screen()
    SHIPS_ON_THE_BOARD = number_of_ships()

    time.sleep(1)
    clear_screen()
    TURNS_OF_PLAY = number_of_turns()

    time.sleep(1)
    clear_screen()

    print_board(board)


if __name__ == '__main__':
    main()
