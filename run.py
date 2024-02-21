import gspread
from google.oauth2.service_account import Credentials
import os

from colorama import init, Fore, Back, Style
init(autoreset=True)

# Authenticate with Google Sheets API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('human_anatomy_quiz')

# Access the 'scoresheet' worksheet
scoresheet = SHEET.worksheet('scoresheet')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    """
    Clears the terminal screen.

    This function uses a system call to clear the
    terminal screen to keep the display clean.
    Recommended to Matt Boden by Goran Sigeskog
    https://github.com/gorsig
    Reccommended to me by my mentor Matt Boden.
    """


def display_instructions():
    """Display the game instructions.

    This function prints out the instructions for the
    Human Anatomy Quiz, explaining how to play,
    including how to answer questions.
    """
    print("\nInstructions:")
    print("Welcome to the Human Anatomy Quiz!")
    print("You will be given a series of questions to test your knowledge.")
    print("Please answer by typing the letter corresponding to your answer",
          "(a, b, c, or d), then press Enter.")
    print("Your final score will be displayed at the end of the quiz.")
    print("After completion of the Quiz")
    print("After completion, if you rank in the top 10,")
    print("your username and score will be added to the leaderboard.")
    print("Good luck!\n")

    input("Press Enter to continue..")


def update_scoresheet(username, score):
    """
    Updates the scoresheet with the username and score.
    Keeps only the top 10 scores and deletes the lowest scores if necessary.
    """
    # Get existing data from the scoresheet
    data = scoresheet.get_all_values()

    # Create a list of tuples containing username and score
    scores = [(row[0], int(row[1])) for row in data[1:]]

    # Add the new score to the list
    scores.append((username, score))

    # Sort scores by score in descending order
    scores.sort(key=lambda x: x[1], reverse=True)

    # Keep only the top 10 scores
    top_scores = scores[:10]

    # Clear the current scoresheet
    scoresheet.clear()

    # Write the updated scores to the scoresheet
    scoresheet.append_row(['Username', 'Score'])
    for username, score in top_scores:
        scoresheet.append_row([username, score])


def new_game(username):
    """
    Start a new game session.

    This function initializes a new game with a set of predefined
    questions. Each question is presented
    to the user along with multiple choice answers. The user's
    responses are evaluated, and feedback is
    provided. The total score is displayed at the end of the session.
    """
    clear()
    questions = [
        #
        {
         "question": "What is the largest organ of the human body?",
         "options": ["a) Heart", "b) Skin", "c) Liver", "d) Kidney"],
         "answer": "b"
        },
        {
         "question": "Which part of the human body produces insulin?",
         "options": ["a) Pancreas", "b) Liver", "c) Kidney", "d) Heart"],
         "answer": "a"
        },
        {
         "question": "What is the largest bone in the human body?",
         "options": ["a) Femur", "b) Tibia", "c) Humerus", "d) Radius"],
         "answer": "a"
        },
        {
         "question": "How many bones are in the human body?",
         "options": ["a) 206", "b) 208", "c) 210", "d) 212"],
         "answer": "a"
        },
        {
         "question": "What is the study of muscles called?", "options":
         ["a) Zoology", "b) Topology", "c) Myology", "d) Xylology"],
         "answer": "c"
        },
        {
         "question": "Which layer of skin is the outermost?", "options":
         ["a) Dermis", "b) Epidermis", "c) Hypodermis", "d) Subcutis"],
         "answer": "b"
        },
        {
         "question": "Where are red blood cells produced?",
         "options": ["a) Heart", "b) Bone marrow", "c) Liver", "d) Spleen"],
         "answer": "b"
        },
        {
         "question": "Where is the patella located?",
         "options": ["a) Arm", "b) Leg", "c) Knee", "d) Foot"],
         "answer": "c"
        },
        {
         "question": "Which of these is a part of the small intestine?",
         "options": ["a) Duodenum", "b) Colon", "c) Cecum", "d) Appendix"],
         "answer": "a"
        },
        {
         "question": "What brain region is key for decision-making?",
         "options": [
          "a) Cerebellum",
          "b) Medulla oblongata",
          "c) Frontal lobe",
          "d) Temporal lobe"
            ],
         "answer": "c"
        }
    ]

    score = 0  # Initialize score

    for q in questions:
        """ For each question, clears the screen,
        displays the question and options, and prompts for an answer.
        """
        clear()
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        while True:
            answer = input("Enter your answer (a, b, c, d):\n").lower()
            if answer not in ["a", "b", "c", "d"]:
                print(Back.RED + "Invalid Answer, Try Again!")
            else:
                break

        # Evaluate the answer and provide feedback.
        if answer == q["answer"]:
            print(Style.BRIGHT + Fore.GREEN + "Correct!" + Style.RESET_ALL)
            score += 1
        else:
            print(Back.RED + "Incorrect. The answer is " + q["answer"] + ".")
        input("Press Enter to continue..")

    clear()
    print(f"\nGame Over {username}! your score was {score}/{len(questions)}")
    print(f"\nYour score will be updated to the leaderboard.")
    print(f"\nCongratulations {username}, if you rank in the top 10.")
    print(f"\nPlease try again if you are not listed on the leaderboard.")
    update_scoresheet(username, score)
    input("Press Enter to return to the menu..")
    """
    Displays the final score and returns to the menu
    """


def menu():
    """
    Displays the main menu and handles user choices.
    This function presents the main menu of the game, allowing
    the user to choose between starting a new game,
    viewing instructions, or quitting. It processes the user's
    input and directs to the appropriate action.
    """

    while True:
        clear()
        print("\nWelcome to the Human Anatomy Quiz Game!")
        print(f"Welcome, {username}!")

        print("1. Play Game")
        print("2. Instructions")
        print("3. Leaderboard")
        print("4. Quit Game")

        choice = input("\nEnter your choice (1-4):\n")

        # Validate user input
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            input("Press Enter to continue..")
            continue

        # Direct the user to the chosen action.
        if choice == "1":
            new_game(username)  # Pass the username as an argument
        elif choice == "2":
            display_instructions()
        elif choice == "3":
            display_leaderboard()
        elif choice == "4":
            print("Sorry to see you leave so soon!")
            break
        else:
            print(Back.RED + "Invalid choice. Please enter 1, 2, 3 or 4.")


def get_valid_username():
    """
    Prompts the user to enter a username, validates it,
    and returns a valid username.

    Returns:
        str: A valid username entered by the user.

    This function repeatedly prompts the user to enter a
    username until a non-empty username containing only letters
    and numbers is provided. It ensures that the
    username adheres to the specified criteria and returns
    it once validated.
    """
    while True:
        username = input("Enter your username:\n").strip()

        if not username:
            print(Back.RED + "Invalid. Please enter a non-empty username.")
            input("Press Enter to continue..")
            continue

        if len(username) > 20:
            print(Back.RED + "Invalid. Maximum character length is 20.")
            input("Press Enter to continue..")
            continue

        if not username.isalnum():
            print(Back.RED + "Invalid. Letters and numbers only.")
            input("Press Enter to continue..")
            continue

        return username


def display_leaderboard():
    clear()
    print("Top 10 Scores:")
    data = scoresheet.get_all_values()
    if len(data) > 1:
        for row in data[1:11]:  # Display top 10 scores
            print(f"{row[0]}: {row[1]}")
    else:
        print("No scores yet.")

    input("Press Enter to return to the menu..")


# Get a valid username from the user
username = get_valid_username()


# Start the game by calling the menu function
menu()
