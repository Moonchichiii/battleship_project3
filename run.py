""" The retry of a new version of battleship game. """
# importing randint,os and time libraries

# from random import randint
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


#time.sleep(5)
#clear_screen()
