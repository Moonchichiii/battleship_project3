


def game_settings():
    size = game_board_size()

def game_board_size():
    size = 0
    while size < 5 or size > 8:
        try:
            size = int(input("Choose the number of rows/cols (5-8): "))
            if size < 5 or size > 8:
                print("invalid size. Please choose between 5 and 8?")
        except ValueError:
            print("Please enter a valid number between 5 and 8")
    return size

board_size = game_board_size()
print(f"test {board_size}")
