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

update_login = SHEET.worksheet('update_login')
login = SHEET.worksheet('login')
existing_user = SHEET.worksheet('existing_user')

data = update_login.get_all_values()
data1 = login.get_all_values()
data2 = existing_user.get_all_values()

print(data, data1, data2)
