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



new_user = login = SHEET.worksheet('new_user')

existing_user = SHEET.worksheet('existing_user')




new_user = update_login.get_all_values()

Look_for_user = existing_user.get_all_values() 

