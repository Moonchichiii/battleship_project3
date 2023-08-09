"""
Import os for 'clear'
Import time for time.delay.
Import random randint for random numbers
"""
import os
import time
from random import randint


def clear_screen():
    """
    Clear the terminal after sign in.

    """
    os.system('clear')


def logo():
    """
    Welcome screen with the logo

    """
    print(r"""
     ___       __  __  __        __   _
    / _ )___ _/ /_/ /_/ ___ ___ / /  (____
   / _  / _ `/ __/ __/ / -_(_-</ _ \/ / _ \
  /____/\_,_/\__/\__/_/\__/___/_//_/_/ .__/
                                  /_/
""")


def welcome():
    """
    Welcome greeting

    """
    print("Ahoy, sailor! to my simple version of battleship!\n")
    print("           Ready to conquer the seas?\n")


def username_prompt():
    """
    username prompt - ask the user to
    provide a valid name

    """
    while True:
        name = input("Please enter your name: ")
        if not name:
            print("Every sailor has a name? Try again!")
        elif name.isnumeric():
            print("Every sailor has a name? Not a number!")
        else:
            break
    return name


def game_settings():
    """
     Game settings

    """
    size = game_board_size()
    ships = number_of_ships()
    turns = number_of_turns()
    return size, ships, turns


def game_board_size():
    """
    verify inputs of the board size 5x5 or 8x8?

    """
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
    """
    verify inputs number of ships on the board

    """
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
    """
    verify inputs number of turns to play

    """
    turns = 0
    while turns < 5 or turns > 10:
        try:
            turns = int(input("How many turns? (5-10): "))
            if turns < 5 or turns > 10:
                print("invalid number of turns! Select a number from! 5 to 10?")
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
    """
    Display the game board in the terminal

    """
    for row in (board):
        print_row = []
        for cell in (row):
            if cell == 'S':
                print_row.append('*')
            else:
                print_row.append(cell)
        print(" ".join(print_row))


def ships_placement(board, total_ships):
    """
    Placing the ships on the board randomly

    """
    placed_ships = 0
    while placed_ships < total_ships:
        row, col = randint(0, len(board) - 1), randint(0, len(board[0]) - 1)
        if board[row][col] != 'S':
            board[row][col] = 'S'
            placed_ships += 1
    return board


def player_turn(board):
    """
    the user picks a row and column for their turn

    """
    max_number_index = len(board)
    while True:
        row = input(f"\nChoose a row (0-{max_number_index}): ")
        col = input(f"Choose a col (0-{max_number_index}): ")
        try:
            row, col = int(row), int(col)
            if 1 <= row <= max_number_index and 1 <= col <= max_number_index:
                break
            else:
                print(f"Please pick a valid number (1-{max_number_index})")
        except ValueError:
            print("Please enter a valid number")

    return row - 1, col - 1


def hit_or_miss(board_with_ships, row, col, sailors_name, hits):
    """
    Checks if the row/col cell contains a 'S'hip, or no ship.
    """
    if board_with_ships[row][col] == 'S':
        board_with_ships[row][col] = 'X'
        print(f"\nGreat job Sailor {sailors_name}! That's a HIT..")
        hits += 1
        return True, hits
    else:
        board_with_ships[row][col] = 'O'
        print(f"\nSorry Sailor {sailors_name}! That's a MISS!..")
        return False, hits


def main():
    """ Main game loop. """

    logo()
    welcome()

    sailors_name = username_prompt()
    print(f"\nWelcome Sailor {sailors_name.upper()}! Sink 'em all!")

    time.sleep(2)
    clear_screen()
    hits = 0

    board_size = game_board_size()
    board = build_board(board_size)

    time.sleep(1)
    clear_screen()
    total_ships = number_of_ships()

    time.sleep(1)
    clear_screen()
    turns_of_play = number_of_turns()

    time.sleep(1)
    clear_screen()

    board_with_ships = ships_placement(board, total_ships)

    while turns_of_play > 0:
        print(f"Ships left: {total_ships}\n")
        print(f"Number of hits: {hits}\n")
        print(f"Turns left: {turns_of_play}\n")
        print_board(board_with_ships)

        row, col = player_turn(board_with_ships)
        hits = hit_or_miss(board_with_ships, row, col, sailors_name, hits)

        turns_of_play -= 1

    if turns_of_play == 0:
        print("Out of Turns! Game over!")


if __name__ == '__main__':
    main()
    while True:
        main()

        restart = input("Ahoy! {sailors_name}! try again? (y/n): ").upper()
        if restart == 'n':
            break
        elif restart == 'y':
            continue
