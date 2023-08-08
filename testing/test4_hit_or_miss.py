from random import randint

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


def ships_placement(board, total_ships):
    """Placing the ships on the board taking the number entered by user """
    placed_ships = 0
    while placed_ships < total_ships:
        row, col = randint(0, len(board) - 1), randint(0, len(board[0]) - 1)
        if board[row][col] != 'S':
            board[row][col] = 'S'
            placed_ships += 1
    return board


board_size = 5
total_ships = 10
name = "john"




board = build_board(board_size)
board_with_ships = ships_placement(board, total_ships)




def hit_or_miss(board, row, col):
    if board[row][col] == 'S':
        print(f"Great job Sailor {name}! That's a HIT..")
        return True
    return False


row, col = randint(0, board_size - 1), randint(0, board_size - 1)
test_hit = hit_or_miss(board_with_ships, row, col)


if test_hit:
    board_with_ships[row][col] = 'X'
else:
    board_with_ships[row][col] = 'M'
print_board(board_with_ships)




