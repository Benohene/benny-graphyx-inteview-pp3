import gspread
from google.oauth2.service_account import Credentials
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('benny_grapyhx-2023')

#the beginning of the main terminal build

FULLNAME = ""

def begin_interview():
    """
    Interview starts with a welcome note from the company,
    moves to candidate to enter full name and get access to instructions,
    then a good will message for the interview
    """
    print("WELCOME TO BENNY GRAPHYX INTERVIEW\n")

    global FULLNAME
    FULLNAME = input("Hello Candidate, Enter your Full Name: \n")

    # if no name is enter, program prompt candidate to enter name
    if FULLNAME == "":
        print("Name is Invalid, Please Enter your Full Name!")
        begin_interview()
    else:
        print(f"\nWelcome to the Job Interview Assessment, {FULLNAME}.\n")
        time.sleep(1)
        print("!!! PLEASE READ CAREFULLY THE INSTRUCTIONS.\n")
        time.sleep(1)
        print("_____________________________________________________________________\n")
        print("THERE ARE 10 INTERVIEW QUESTION, THIS WILL HELP US ASSESS YOU WELL.\n")
        time.sleep(1)
        print("EACH QUESTION COMES WILL 4 MULTI CHIOCE ANSWERS.\n")
        time.sleep(1)
        print("ENTER THE ANSWER FOR OPTIONS A,B,C AND D AND HIT ENTER.\n")
        time.sleep(1)

        start_interview = input("ARE YOU READY FOR THE INTERVIEW? (Y)YES or (N)NO: ")
        if start_interview.lower() != "y":
            quit()

        print("LETS GET ON - GOOD LUCK :)")
        

# ------------------------

"""def interview_main():

def check_answer():

def display'''

#create dictionary of questions awith answers and options to choose from
"""

begin_interview()