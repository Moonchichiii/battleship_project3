""" The retry of a new version of battleship game. """

# rules of the game (logic) # legend
# 1. single player game
# 2. user inputs username (display name)
# 3. user inputs for the size of the board 5x5 or 8x8 rows/cols
# 4. user inputs number of ships
# 5. user inputs number of turns
# 6. computer sets out the random ships
# 7. user inputs what row then coloum.
# 8. verify the user input
# 9. display name?
# 10. hits and misses

# importing randint,os and time libraries


from random import randint
import os
import time


def clear_screen():
    """Clear the terminal after sign in."""
    os.system('clear')


def logo():
    """Welcome game logo"""
    print(r"""
   ___       __  __  __        __   _
  / _ )___ _/ /_/ /_/ ___ ___ / /  (____
 / _  / _ `/ __/ __/ / -_(_-</ _ \/ / _ \
/____/\_,_/\__/\__/_/\__/___/_//_/_/ .__/
                                  /_/
""")


def welcome():
    """Welcome greeting"""
    print("Welcome to my simple version of battleship!\n")


#  calling the logo first and the greeting text.
logo()
welcome()


name = input("Please enter your name: ")
"""username input while loop"""
while not name:
    print("Every sailor has a name? try again!")
    name = input("Please enter your name: ")
else:
    print(f"\nWelcome aboard {name}! Ready to sink some ships?")


time.sleep(3)
clear_screen()


#  user inputs for the size of the board 5x5 or 8x8 rows/cols
#  user inputs amount of ships 2-6


def game_settings():
    size = game_board_size()
    ships = number_of_ships()


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


board_size = game_board_size()
print(f"test {board_size}")

time.sleep(2)
clear_screen()


def number_of_ships():
    ships = 0
    while ships < 2 or ships > 6:
        try:
            ships = int(input("How many ships would you like on the board?: "))
            if ships < 2 or ships > 6:
                print("invalid number of ships! Please choose between 2 or 6?")
        except ValueError:
            print("Please enter a valid number between 2 and 6")
    return ships


ships_on_the_board = number_of_ships()
print(f"number of ships {ships_on_the_board}")
