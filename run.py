import os
import sys
import time

def display_instructions():
    print("\nInstructions:")
    print("Welcome to the Human Anatomy Quiz!")
    print("You will be given a series of questions to test your knowledge.")
    print("Please answer by typing the letter corresponding to your answer (a, b, c, or d), then press Enter.")
    print("Good luck!\n")

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears the screen
        print("\nWelcome to the Human Anatomy Quiz Game!")
        print("1. Play Game")
        print("2. Instructions")
        print("3. Quit Game")

        choice = input("\nEnter your choice (1-3):\n")
        
        if choice == "1":
            new_game()
        elif choice == "2":
            display_instructions()
        elif choice == "3":
            print("Sorry to see you leave so soon!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")