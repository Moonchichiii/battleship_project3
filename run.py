""" The retry of a new version of battleship game. """

# rules of the game (logic) # legend. 
# 1. single player game
# 2. user inputs username (display name)
# 3. user inputs for the size of the board 5x5 or 8x8 rows/cols
# 4. user inputs number of ships 
# 5. user inputs number of turns
# 6. computer sets out the random ships
# 7. user inputs what row then coloum.
# 8. verify the user input
# 9. 


# importing randint,os and time libraries

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
while not name:
    print("Every sailor has a name? try again.!")
    name = input("Please enter your name: ")

    print(f"Welcome aboard {name}! Ready to sink some ships?")


time.sleep(5)
clear_screen()


def game_settings():
    pass


def game_board_size():
    pass

    