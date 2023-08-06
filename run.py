""" The retry of a new version of battleship game. """

from random import randint
import os
import time


# importing randint,os and time libraries


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
    print("Ahoy, sailor! to my simple version of battleship!\n")
    print("           Ready to conquer the seas?\n")


#  calling the logo first and the greeting text.
logo()
welcome()


name = input("Please enter your name: ")
"""username input while loop"""
while not name:
    print("Every sailor has a name? try again!")
    name = input("Please enter your name: ")
else:
    print(f"\nWelcome aboard Sailor {name}! Ready to sink some ships! Or sink to depths!")


time.sleep(2)
clear_screen()


#  user inputs for the size of the board 5x5 or 8x8 rows/cols
#  user inputs amount of ships 2-6


def game_settings():

    # return to these once the BOARD LOOP is ready to
    # take these inputs! TEMPORARY INPUT REMOVE ONCE DONE!

    """ Set game settings """
    #size = game_board_size()
    #ships = number_of_ships()
    #turns = number_of_turns()


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

time.sleep(1)
clear_screen()


def number_of_ships():
    """  verify inputs number of ships on the board """
    ships = 0
    while ships < 2 or ships > 6:
        try:
            ships = int(input("How many ships on the board? (2-6): "))
            if ships < 2 or ships > 6:
                print("invalid number of ships! Please choose between 2 or 6?")
        except ValueError:
            print("Please enter a valid number between 2 and 6")
    return ships


SHIPS_ON_THE_BOARD = number_of_ships()
print(f"number of ships {SHIPS_ON_THE_BOARD}")

time.sleep(1)
clear_screen()


def number_of_turns():
    """  verify inputs number of turns to play """
    turns = 0
    while turns < 5 or turns > 10:
        try:
            turns = int(input("How many turns? (5-10): "))
            if turns < 5 or turns > 10:
                print("invalid number of turns! Choose between 5 or 10?")
        except ValueError:
            print("Please enter a valid number between 5 and 10")
    return turns


TURNS_OF_PLAY = number_of_turns()
print(f"number of turns {TURNS_OF_PLAY}")

time.sleep(1)
clear_screen()

#print(f"rows/cols {BOARD_SIZE} \n")
#print(f"ships     {SHIPS_ON_THE_BOARD} \n")
#print(f"turns     {TURNS_OF_PLAY} \n")



