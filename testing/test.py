

"""
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
print(f"test {board_size}") """

def number_of_turns():
    turns = 0
    while turns < 5 or turns > 10:
        try:
            turns = int(input("How many turns? (5-10): "))
            if turns < 5 or turns > 10:
                print("invalid number of turns! Please choose between 5 or 10?")
        except ValueError:
            print("Please enter a valid number between 5 and 10")
    return turns


turns_of_play = number_of_turns()  
print(f"number of turns {turns_of_play}")  # wrong referenching <---- turns_of_play! 
