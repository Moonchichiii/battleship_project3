def hit_or_miss(board_with_ships, row, col, sailors_name):
    if board_with_ships[row][col] == 'S':
        board_with_ships[row][col] = 'X'
        print(f"Great job Sailor {sailors_name}! That's a HIT..")
        return True

        board_with_ships[row][col] = 'M'
        print(f"Sorry Sailor {sailors_name}! That's a MISS!..")
        return False

board = build_board(board_size)
hit_or_miss(board_with_ships, row, col, sailors_name)