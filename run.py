""" The retry of a new version of battleship game. """
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
