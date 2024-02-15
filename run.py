import os
import sys
import time


def clear():
    os.system('cls' if os.name == 'nt' 'clear')
    """
    Clears the terminal screen.

    This function uses a system call to clear the
    terminal screen to keep the display clean.
    Recommended to Matt Boden by Goran Sigeskog
    https://github.com/gorsig
    Reccommended to me by my mentor Matt Boden
    """"


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
    print("Good luck!\n")


def new_game():
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
        answer = input("Enter your answer (a, b, c, d):\n").lower()

        # Evaluate the answer and provide feedback.
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer was " + q["answer"] + ".")

    clear()
    print(f"\nGame Over! Your score was {score}/{len(questions)}")
    input("Press Enter to return to the menu...")
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
        print("1. Play Game")
        print("2. Instructions")
        print("3. Quit Game")

        choice = input("\nEnter your choice (1-3):\n")
        # Direct the user to the chosen action.
        if choice == "1":
            new_game()
        elif choice == "2":
            display_instructions()
        elif choice == "3":
            print("Sorry to see you leave so soon!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Starts the game by calling the menu function.


menu()
