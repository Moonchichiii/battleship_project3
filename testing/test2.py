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
    for i, row in enumerate(board):
        print_row = []
        for j, cell in enumerate(row):
            if cell == 'S':
                print_row.append('*')
            else:
                print_row.append(cell)
        print(" ".join(print_row))

