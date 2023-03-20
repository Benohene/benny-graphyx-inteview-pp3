"""
All import for the interview terminal
"""
# import time for time sleep
import time

# import gspread for marks recording
import gspread
from google.oauth2.service_account import Credentials

# import pyfiglet module for ascii art
import pyfiglet

# import colorama for adding colour
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('benny_grapyhx-2023')

# the beginning of the main terminal build

FULLNAME = ""


def begin_interview():
    """
    The interview starts with a welcome note from the company
    moves to the candidate to enter the full name
    instructions,then a goodwill message for the interview
    """
    print("________________________________\n")
    print(f"{Back.RED}WELCOME TO INTERVIEW ASSESSMENT")
    print("________________________________")
    print(pyfiglet.figlet_format("BENNY GRAPHYX"))

    global FULLNAME
    FULLNAME = input("Hello Candidate, Enter your Full Name:\n")

    # if no name is entered, prompts the candidate to enter the name
    if FULLNAME == "":
        print("Hello Candidate, Enter your Full Name:\n")
        begin_interview()
    else:
        print(f"\nWelcome to the Job Interview Assessment, {FULLNAME}.\n")
        time.sleep(1)
        print("!!! PLEASE READ CAREFULLY THE INSTRUCTIONS.")
        time.sleep(1)
        print("________________________________\n")
        print("1. THERE ARE 10 INTERVIEW QUESTION.\n")
        time.sleep(1)
        print("2. EACH QUESTION COMES WILL 4 MULTI CHIOCE ANSWERS.\n")
        time.sleep(1)
        print("3. ENTER THE ANSWER FOR OPTIONS A,B,C AND D AND HIT ENTER.\n")
        time.sleep(1)
        print("________________________________\n")

    while True:
        start_interview = input(
            "ARE YOU READY FOR THE INTERVIEW? (Y)YES or (N)NO: \n")

        if start_interview.lower() != "y" and start_interview.lower() != "n":
            print(f"{Fore.RED}INVALID ENTRY, PUT IN THE RIGHT VALUE Y/N \n")
            continue

        elif start_interview.lower() == "y":
            print("__________________________________________\n")
            print("LETS GET ON - GOOD LUCK .\n")
            time.sleep(2)
            break
        else:
            print("________________________________\n")
            print("GOOD BYE, SEE YOU NEXT TIME \n")
            time.sleep(1)
            quit()
            break


# set up the interview questions and options to link the dictionary


def interview_main():
    """
    this function will loop the questions and answers in the dictionary
    of questions and options
    """

    print(f"{Fore.CYAN}INTERVIEW QUESTIONS")
    choices = []
    correct_choices = 0
    question_numbers = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_numbers-1]:
            print(i)
        choice = input("Enter (A, B, C, or D): ")
        choice = choice.upper()
        choices.append(choice)

        correct_choices += check_answer(questions.get(key), choice)
        question_numbers += 1

    display_marks(correct_choices, choices)


# Check for answer and print CORRECT or WRONG
def check_answer(answer, choice):
    """
    check through user answer provided
    print CORRECT or WRONG
    """

    if answer == choice:
        print(f"{Fore.GREEN}CORRECT")
        return 1
    else:
        print(f"{Fore.RED}WRONG")
        return 0

# display mark on terminal


def display_marks(correct_choices, choices):
    """
    display candidate answers and correct answers
    display marks after all questions have been answered
    display marks in percentage%
    """

    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Choices: ", end="")
    for i in choices:
        print(i, end=" ")
    print()

    mark = int((correct_choices / len(questions)) * 100)
    print("Your Mark is: " + str(mark) + "% \n")

# display message for outcome of the interview
    print("-------------------------------------\n")
    if mark >= 60:
        print(f"{Fore.GREEN}CONGRATULATION; YOU ARE QUALIFIED \n")
    elif mark < 60:
        print(f"{Fore.RED}SORRY, YOU ARE DISQUALIFIES \n")

    candidate_marks = FULLNAME, mark
    export_marks(candidate_marks)


# create dictionary of questions awith answers and options to choose from
questions = {
    "1. Which one shows the pattern?: ": "C",
    "2. Organizing and composing words and images to create a message: ": "A",
    "3. A print is made from a metal, wood, or plastic plate.: ": "D",
    "4. The areas around, above, between, below, or within something.: ": "D",
    "5. Color schemes that use colors side by side have a common hue.: ": "B",
    "6. Lightness or darkness of a color. ": "D",
    "7. Which of the following is any plan for organizing colors: ": "A",
    "8. This Art helps to organized rules for dynamical process: ": "C",
    "9. The primary colors mixed to create white light: ": "D",
    "10.Signatures are carved, dipped in ink, and pressed onto paper.": "A"
}

options = [
    ["A. Texture", "B. Temperature", "C. Template", "D. Tonality"],
    ["A. Graphic design", "B. Optical illusion", "C. Illusion",
        "D. Expression"],
    ["A. Insignia", "B. Branding", "C. Harmony", "D. Engravings"],
    ["A. Balance", "B. Value", "C. Hue", "D. Space"],
    ["A. Color scheme", "B. Analogous color scheme",
        "C. Monochromatic color scheme", "D. Triad color scheme"],
    ["A. Variety", "B. Space", "C. Balance", "D. Value"],
    ["A. Color Scheme", "B. Color Wheel", "C. Composition", "D. Closure"],
    ["A. Optical illusion", "B. The elements of art/design",
        "C. Principles of design", "D. Graphic design"],
    ["A. Chop marks", "B. Temperature", "C. Template",
        "D. Additive primaries"],
    ["A. Chop marks", "B. Watermark", "C. Closure", "D. Trademark"]
]


# Export results based on Love Sandwiches project by CI
def export_marks(candidate_marks):
    """
    export the marks of the interview including
    the candidate's name and final marn to the overall mark worksheet
    """
    print("Updating Candidate Marks to worksheet...\n")
    time.sleep(2)
    results_worksheet = SHEET.worksheet("overall_marks")
    results_worksheet.append_row(candidate_marks)
    print("Candidate Marks exported to worksheet successfully \n")
    time.sleep(1)


begin_interview()
interview_main()

print("--------------------------------------------------------")
print("THANK YOU FOR APPLYING TO OUR COMPANY \n")
