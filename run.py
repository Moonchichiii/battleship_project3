""" Imported libraries """
import os
import time
from random import randint
import gspread
from google.oauth2.service_account import Credentials
import bcrypt


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


# Constants for Game Layout.
BOARD_DESIGN = '*'
HIT_SHIP = 'X'
MISS = 'M'
SHIP = 'S'


def welcome():
    """ Greetings message """

    print("        Ahoy, sailor! Ready to conquer the seas?\n")
    print("\nInstructions....\n")
    print("1. If you have played before, then just press Y to login.")
    print("2. New here? then create a user and a simple password to remember")
    print("3. Or want to Exit? this is your chance, press 'E' to Exit... \n")


def clear_screen():
    """ Clear screen in the terminal """
    os.system('clear')


def logo():
    """ Game Logo."""

    print(r"""
  ____          _    _    _             _      _
 |  _ \        | |  | |  | |           | |    (_)
 | |_) |  __ _ | |_ | |_ | |  ___  ___ | |__   _  _ __
 |  _ <  / _` || __|| __|| | / _ \/ __|| '_ \ | || '_ \
 | |_) || (_| || |_ | |_ | ||  __/\__ \| | | || || |_) |
 |____/  \__,_| \__| \__||_| \___||___/|_| |_||_|| .__/
                                                 | |
                                                 |_|
""")


def main_menu():
    """ Main sign in prompt."""

    while True:
        choices = input("\n\nHave you played before? (y/n)?: ").upper()
        if choices == 'Y':
            username = login(user_sheet)
            if username:
                return username
        elif choices == 'N':
            username = create_auth(user_sheet)
            if username:
                print(f"Welcome {username}! Let's Play!")
                return username
        elif choices == 'E':
            print("\nThank you for stopping by! Exiting....")
            exit()
        print("\nInvalid Choice! Try Again...")


def create_auth(worksheet):
    """create new user in the spreadsheet"""
    attempt = 0
    attempt_limit = 3

    while True:
        username = input("\nPlease enter A username: ").strip().lower()
        if not username:
            print("\nEvery sailor has a name? Try again!")
            continue
        elif username.isnumeric():
            print("\nEvery sailor has a name? Not a number!")
            continue

        password = input("\nPlease select A password: ")

        if not user_exists(username, worksheet):
            ha_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            worksheet.append_row([username, ha_pw])
            print("\nSign up successful....")
            return username
        else:
            print("\nPasswords do not match! try again...")
            attempt += 1

        if attempt >= attempt_limit:
            print("\nMaximum attempts reached! try again...")
            exit()


def user_exists(username, worksheet):
    """ Check f the user has already registered """

    column_values = worksheet.col_values(1)
    if username in column_values:
        return username in column_values


def login(worksheet):
    """ Checks if the username and password exists in "user_sheet" """
    attempt = 0
    attempt_limit = 3

    while True:
        username = input("\nEnter your username: ").strip().lower()
        password = input("\nEnter your password: ")

        if user_exists(username, worksheet):
            try:
                cell = worksheet.find(username)
                ha_pw = worksheet.cell(cell.row, cell.col + 1).value.encode()

                if bcrypt.checkpw(password.encode(), ha_pw):
                    print("\nLogin successful......")
                    return username
                else:
                    print("\nIncorrect password. Please try again.")
                    attempt += 1
                if attempt >= attempt_limit:
                    print("\nMaximum attempts reached! try again...")
                    exit()
            except ValueError:
                print("\nA error occurred during processing...")
        else:
            print("\nInvalid username, try again")
            attempt += 1
            if attempt >= attempt_limit:
                print("\nMaximum attempts reached! try again...")
                exit()


def game_settings():
    """
     User Game settings.
     board size (5x5 or 8x8),
     number of ships (2 or 6),
     number of turns (5 to 10),

    """
    size = game_board_size()
    ships = number_of_ships()
    turns = number_of_turns()
    return size, ships, turns


def game_board_size():
    """ Validate user chosen board size (5x5 or 8x8) """

    size = 0
    while size != 5 and size != 8:
        try:
            size = int(input("Select board size (5x5 or 8x8): "))
            if size != 5 and size != 8:
                print("Invalid size. Please choose between (5x5 or 8x8)?")
        except ValueError:
            print("Please select a valid! board size (5x5 or 8x8)")
    return size


def number_of_ships():
    """ Validate users selected number of ships. """
    ships = 0
    while ships < 2 or ships > 6:
        try:
            ships = int(input("Choose the number of ships? (2-6): "))
            if ships < 2 or ships > 6:
                print("Invalid number! Please choose between 2 and 6 ships?")
        except ValueError:
            print("Please enter a valid number between 2 and 6")
    return ships


def number_of_turns():
    """ Validate users selected number of game turns """
    turns = 0
    while turns < 5 or turns > 10:
        try:
            turns = int(input("How many turns ? (5-10): "))
            if turns < 5 or turns > 10:
                print("invalid turns! Select a number from (5 to 10)?")
        except ValueError:
            print("Please enter a valid number between (5 and 10)")
    return turns


def build_board(size):
    """ Creates game board after chosen size (5x5 or 8x8). """

    return [[BOARD_DESIGN for _ in range(size)] for _ in range(size)]


def print_board(board):
    """ Display the game board in the terminal """
    for row in (board):
        print_row = []
        for cell in (row):
            if cell == SHIP:
                print_row.append(BOARD_DESIGN)
            else:
                print_row.append(cell)
        print(" ".join(print_row))


def ships_placement(board, total_ships):
    """ Randomly placing ships on the board,
    total_ships selected number of ships. """

    placed_ships = 0
    while placed_ships < total_ships:
        row, col = randint(0, len(board) - 1), randint(0, len(board[0]) - 1)
        if board[row][col] != SHIP:
            board[row][col] = SHIP
            placed_ships += 1
    return board


def player_turn(board):
    """ User choose a row and column for their turn based on board size.
        Returns chosen row and column """

    max_number_index = len(board)
    while True:
        row = input(f"\nChoose a row (0-{max_number_index}): ")
        col = input(f"Choose a col (0-{max_number_index}): ")
        try:
            row, col = int(row), int(col)
            if 1 <= row <= max_number_index and 1 <= col <= max_number_index:
                break
            else:
                print(f"Please pick a valid number (1-{max_number_index})")
        except ValueError:
            print("Please enter a valid number")

    return row - 1, col - 1


def hit_or_miss(board_with_ships, row, col, sailors_name):
    """ Validate if row/col contains a ship 'S' or not."""

    if board_with_ships[row][col] == SHIP:
        board_with_ships[row][col] = HIT_SHIP
        print(f"\nGreat job Sailor {sailors_name}! That's a HIT..\n")
        return True
    else:
        board_with_ships[row][col] = MISS
        print(f"\nSorry Sailor {sailors_name}! That's a MISS!..\n")
        return False


def main():
    """ Game loop """

    logo()
    welcome()

    sailors_name = main_menu()

    if not sailors_name:
        print("Thank for stopping by...")
        return
    print(f"\nWelcome Sailor {sailors_name.upper()} ! Sink 'em all!")

    time.sleep(5)
    clear_screen()

    board_size = game_board_size()
    board = build_board(board_size)

    time.sleep(1)
    clear_screen()
    total_ships = number_of_ships()

    time.sleep(1)
    clear_screen()
    turns_of_play = number_of_turns()

    time.sleep(1)
    clear_screen()

    board_with_ships = ships_placement(board, total_ships)

    hits = 0

    while turns_of_play > 0 and hits < total_ships:
        print(f"Ships left: {total_ships}\n")
        print(f"Number of hits: {hits}\n")
        print(f"Turns left: {turns_of_play}\n")
        print_board(board_with_ships)

        row, col = player_turn(board_with_ships)
        got_hit = hit_or_miss(board_with_ships, row, col, sailors_name)
        if got_hit:
            total_ships -= 1
            hits += 1

        turns_of_play -= 1

    if turns_of_play == 0:
        print("\nOut of Turns! Game over!")

    if hits == total_ships:
        print(f"\nAhoy! {sailors_name}! Out of ships! victorious!")


if __name__ == '__main__':
    while True:
        main()
        restart = input("\nAhoooy Sailor! try again? (y/n): ").upper()

        if not restart:
            print("\nPlease confirm with (y/n) ? Try again!")

        elif restart == 'N':
            print("\nThank you for playing!")
            exit()

        elif restart == 'Y':
            clear_screen()
            continue

        elif restart.isnumeric():
            print("\nPlease confirm with (y/n) ? Not a number!")

        else:
            print("\nInvalid input! Please confirm with (y/n) ?")
