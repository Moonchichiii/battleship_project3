
def game_settings():
    """ Set game settings """
    size = game_board_size()
    return size


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




def build_board(size):
    """
    Builds the game board and filled with '*'

    Size int the number of rows and columns from user input size.
    """
    return [['*' for _ in range(size)] for _ in range(size)]


def print_board(board):
    for row in board:
        print(" ".join (row))

BOARD_SIZE = game_settings()
print_board(board)
