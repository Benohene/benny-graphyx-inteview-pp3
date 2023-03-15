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
"""

#create dictionary of questions awith answers and options to choose from
questions = {
"1.  Which one shows the pattern?: ": "C",
"2.  Which process of organizing and composing words and images to create a message?: ": "A",
"3.  A technique in which design is incised in a metal, wood, or plastic plate. A print is then made from the plate.: ": "D",
"4.  Which shows the areas around, above, between, below, or within something?: ": "D",
"5.  Which color scheme that uses colors side by side have a common hue on the color wheel?: ": "B",
"6.  which of the following is similar, lightness or darkness of a color: ": "D",
"7.  Which of the following is any plan for organizing colors: ": "A",
"8.  The elements of art the principle that help to organized rules for dynamical: ": "C",
"9.  which are the primary colors of light red, green, and blue which create white light when mixed together: ": "D",
"10. which one is a signatures carved in wood, dipped in ink, and pressed onto paper or canvas to identify their work: ": "A"
}

options = [
["A. Texture", "B. Temperature", "C. Template", "D. Tonality"],
["A. Graphic design", "B. Optical illusion", "C. Illusion", "D. Expression"],
["A. Insignia", "B. Branding", "C. Harmony", "D. Engravings"],
["A. Balance", "B. Value", "C. Hue", "D. Space"],
["A. Color scheme", "B. Analogous color scheme", "C. Monochromatic color scheme", "D. Triad color scheme"],
["A. Variety", "B. Space", "C. Balance", "D. Value"],
["A. Color Scheme", "B. Color Wheel", "C. Composition", "D. Closure"],
["A. Optical illusion", "B. The elements of art/design", "C. Principles of design", "D. Graphic design"],
["A. Chop marks", "B. Temperature", "C. Template", "D. Additive primaries"],
["A. Chop marks", "B. Watermark", "C. Closure", "D. Trademark"]
]

begin_interview()