import os
import sys
import time


def display_instructions():
    print("\nInstructions:")
    print("Welcome to the Human Anatomy Quiz!")
    print("You will be given a series of questions to test your knowledge.")
    print("Please answer by typing the letter corresponding to your answer",
          "(a, b, c, or d), then press Enter.")
    print("Good luck!\n")


def new_game():
    questions = [
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
    ]

    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (a, b, c, d):\n").lower()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer was " + q["answer"] + ".")

    print(f"\nGame Over! Your score was {score}/{len(questions)}")
    input("Press Enter to return to the menu...")


def menu():
    while True:
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


menu()
