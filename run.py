import os
import sys
import time

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