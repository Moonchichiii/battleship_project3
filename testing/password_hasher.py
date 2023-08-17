""" Imported libraries """
import os
import gspread
from google.oauth2.service_account import Credentials
from argon2 import PasswordHasher


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.Client(auth=SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('battleship')
user_sheet = SHEET.worksheet('users')
# Using the Argon2 password hasher.
ph = PasswordHasher()


def main_menu():
    """ New sign in prompt."""
    while True:
        choices = input("\nHave you played before? (y/n)?:  ").upper()
        if choices == 'Y':
            username = login()
            if username:
                return username
        elif choices == 'N':
            username = create_auth()
            if username:
                print(f"Welcome {username}! Let's Play!")
                return username
        elif choices == 'E':
            print("\nThank you for stopping by! Exiting....")
            exit()
        print("nInvalid Choice! Try Again...")

def create_auth():
    """create new user in the spreadsheet"""
    while True:
        username = input("Please enter A username: ").strip().lower()
        if not username:
            print("\nEvery sailor has a name? Try again!")
            continue
        elif username.isnumeric():
            print("\nEvery sailor has a name? Not a number!")
            continue

        password = input("Please select A password: ")
        password_confirm = input("Please confirm your password: ")

        if password == password_confirm:
            if not user_exists(username, user_sheet):
                hashed_pswd = ph.hash(password)
                user_sheet.append_row([username, hashed_pswd])
                print("Sign up successful.....Welcome ")
                return username

            else:
                print("Username already exists! Try again...")
        else:
            print("Passwords do not match! Try again...")


def user_exists(username, worksheet):
    """ Check f the user has already registered """

    column_values = worksheet.col_values(1)
    if username in column_values:
        print(f"Found username '{username}'.")
        return username in column_values


def login():
    """ Checks if the username and password exists in "user_sheet" """
    while True:
        username = input("Enter your username: ").strip().lower()
        password = input("Enter your password: ").strip().lower()

        if user_exists(username, user_sheet):
            cell = user_sheet.find(username)
            hashed_pswd = user_sheet.cell(cell.row, cell.col + 1).value.strip()
            hashed_pswd_return = hashed_pswd.decode('utf-8')
            print(hashed_pswd_return)
            if ph.verify(password, hashed_pswd_return):
                print(f"Super Welcome {username.upper()}! Login successful..")
                return username
            else:
                print("Invalid Password! Try again...")
        else:
            print("Invalid username, try again, or create a new account....")



def main():
    """ Game loop """

    logo()
    welcome()

    sailors_name = main_menu()

    if not sailors_name:
        print("Thank for stopping by...")
        return
    print(f"\nWelcome Sailor {sailors_name.upper()}! Sink 'em all!")


if __name__ == '__main__':
    while True:
        main()
        