""" Imported libraries """
import os
import time
from random import randint


def clear_screen():
    """ Clear screen in the terminal """
    os.system('clear')


def logo():
    """ Game Logo."""

    print(r"""
     ___       __  __  __        __   _
    / _ )___ _/ /_/ /_/ ___ ___ / /  (____
   / _  / _ `/ __/ __/ / -_(_-</ _ \/ / _ \
  /____/\_,_/\__/\__/_/\__/___/_//_/_/ .__/
                                  /_/
""")


def welcome():
    """ Greetings message """

    print("Ahoy, sailor! Welcome to a simple version of battleship!\n")
    print("           Ready to conquer the seas?\n")


def username_prompt():
    """
    User prompt for game name.
    Check if the line is empty or contains just numbers.

    """
    while True:
        name = input("Please enter your name: ")
        if not name:
            print("\nEvery sailor has a name? Try again!")
        elif name.isnumeric():
            print("\nEvery sailor has a name? Not a number!")
        else:
            break
    return name


def game_settings():
    """
     User Game settings.
     board size (5x5 or 8x8),
     number of ships (2 or 6),
     number of turns (5 to 10),

    """
    size = game_board_size()
    ships = number_of_ships()
    turns = number_of_turns()
    return size, ships, turns


def game_board_size():
    """ Validate user chosen board size (5x5 or 8x8) """

    size = 0
    while size != 5 and size != 8:
        try:
            size = int(input("Select board size (5x5 or 8x8): "))
            if size != 5 and size != 8:
                print("Invalid size. Please choose between (5x5 or 8x8)?")
        except ValueError:
            print("Please select a valid! board size (5x5 or 8x8)")
    return size


def number_of_ships():
    """ Validate users selected number of ships. """
    ships = 0
    while ships < 2 or ships > 6:
        try:
            ships = int(input("Choose the number of ships? (2-6): "))
            if ships < 2 or ships > 6:
                print("Invalid number! Please choose between 2 and 6 ships?")
        except ValueError:
            print("Please enter a valid number between 2 and 6")
    return ships


def number_of_turns():
    """ Validate users selected number of game turns """
    turns = 0
    while turns < 5 or turns > 10:
        try:
            turns = int(input("How many turns ? (5-10): "))
            if turns < 5 or turns > 10:
                print("invalid turns! Select a number from (5 to 10)?")
        except ValueError:
            print("Please enter a valid number between (5 and 10)")
    return turns


def build_board(size):
    """ Creates game board after chosen size (5x5 or 8x8). """

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
    """ Randomly placing ships on the board,
    total_ships selected number of ships. """

    placed_ships = 0
    while placed_ships < total_ships:
        row, col = randint(0, len(board) - 1), randint(0, len(board[0]) - 1)
        if board[row][col] != 'S':
            board[row][col] = 'S'
            placed_ships += 1
    return board


def player_turn(board):
    """ User choose a row and column for their turn based on board size.
        Returns chosen row and column """

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


def hit_or_miss(board_with_ships, row, col, sailors_name):
    """ Validate if row/col contains a ship 'S' or not."""

    if board_with_ships[row][col] == 'S':
        board_with_ships[row][col] = 'X'
        print(f"\nGreat job Sailor {sailors_name}! That's a HIT..\n")
        return True
    else:
        board_with_ships[row][col] = 'O'
        print(f"\nSorry Sailor {sailors_name}! That's a MISS!..\n")
        return False


def main():
    """ Main game loop. """

    logo()
    welcome()

    sailors_name = username_prompt()
    print(f"\nWelcome Sailor {sailors_name.upper()}! Sink 'em all!")

    time.sleep(3)
    clear_screen()

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

    hits = 0

    while turns_of_play > 0 and hits < total_ships:
        print(f"Ships left: {total_ships}\n")
        print(f"Number of hits: {hits}\n")
        print(f"Turns left: {turns_of_play}\n")
        print_board(board_with_ships)

        row, col = player_turn(board_with_ships)
        got_hit = hit_or_miss(board_with_ships, row, col, sailors_name)
        if got_hit:
            total_ships -= 1
            hits += 1

        turns_of_play -= 1

    if turns_of_play == 0:
        print("\nOut of Turns! Game over!")

    if hits == total_ships:
        print(f"\nAhoy! {sailors_name}! Out of ships! victorious!")


if __name__ == '__main__':
    while True:
        main()

        restart = input("\nAhoooy Sailor! try again? (y/n): ").upper()

        if not restart:
            print("\nPlease confirm with (y/n) ? Try again!")
            continue
        
        elif restart == 'N':
            print("\nThank you for playing!")
            break

        
        elif restart == 'Y':
            continue
        elif restart.isnumeric():
            print("nPlease confirm with (y/n) ? Not a number!")
        else:
            print("nInvalid input! Please confirm with (y/n) ?")
