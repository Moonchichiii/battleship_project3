""" imported libaries """

import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)


SHEET = GSPREAD_CLIENT.open('battleship')
user_sheet = SHEET.worksheet('users')



print("Ahoy, sailor! Ready to conquer the seas?\n")
print("in this simple version of battleship!\n")
Print("\n \n Instructions....")
Print("If you have played before, then just put Y and login.")
Print("If Not you have to create a user with a simple password to remeber")
Print("Or you want to exit this is your chance, with 'E' to Exit the game")



def main_menu():
    """ New sign in prompt."""
    while True:
        try:
            choices = input("\nHave you played before? (y/n)?:  ").upper()

            if choices == 'Y':
                login()
            elif choices == 'N':
                create_auth()
            elif choices == 'E':
                print("\nThank you! Exiting.......")
                break
            else:
                print("nInvalid Choice! Try Again...")
        except ValueError:
            print("\nEnter a Valid Choice (y/n) or ('Q') to Exit : ")


main_menu()


def create_auth():
    """create new user in the spreadsheet"""


def users_exists():
    """Check if the user exists in the file already """


def login():
    """Login if you have played before."""

