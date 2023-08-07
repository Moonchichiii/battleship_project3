""" import """
import os
import time


def clear_screen():
    """Clear and refresh the terminal display during the game """
    os.system('clear')


def main():
    """ Validate and check the value input to build the board 5x5 or 8x8 """
    board_size = game_board_size()
    board = build_board(board_size)
    """Clear and refresh the terminal display during the game """
    time.sleep(2)
    clear_screen()
    print_board(board)


def game_settings():
    """ Set game settings """
    size = game_board_size()
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


def build_board(size):
    """
    Builds the game board and filled with '*'

    Size int the number of rows and columns from user input size.
    """
    return [['*' for _ in range(size)] for _ in range(size)]


def print_board(board):
    """ Display the game board in the terminal """
    for row in board:
        print(" ".join(row))


if __name__ == '__main__':
    main()
