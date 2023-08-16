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
                hashed_password = ph.hash(password)
                user_sheet.append_row([username, hashed_password])
                print("Sign up successful.....Welcome ")
                break
            else:
                print("Username already exists! Try again...")
        else:
            print("Passwords do not match! Try again...")


def user_exists(username, worksheet):
    """ Check f the user has already registered """

    column_values = worksheet.col_values(1)
    if username in column_values:
        print(f"Found username '{username}'.")
        return True
    return False


def login():
    while True:
        password = input("Please select A password: ").strip().lower()
        password_confirm = input("Please confirm your password: ")

    if user_exists(username, user_sheet):
        cell = user_sheet.find(Username)
        stored_hashed_password = user_sheet.cell(cell.row, cell .col)
        if ph.verify(stored_hashed_password, password):
            print(f"Super Welcome {username.upper()}! Login successful....")
            break
        else:
            print("Invalid Password! try again...")
    else:
        print("Invalid  usernane, try again, or create a new account....")
