
def build_board(size):
    """
    Builds the game board and filled with '*'

    Size int the number of rows and columns from user input size.

    """
board_with_ships = build_board(5)

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


def player_turn(board, turns):

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



def main():
    """ Main game loop. """
    
    hits = 0
    turns = 0

    while turns < 5 or turns > 10:
        
        
        try:
        
            if 
               
            
            
        except ValueError:
            print("Please enter a valid number")
            
    return turns

    print_board(board_with_ships)
    row, col = player_turn(board_with_ships, turns_of_play)
    hits = hit_or_miss(board_with_ships, row, col, sailors_name, hits)


if __name__ == '__main__':
    main()
