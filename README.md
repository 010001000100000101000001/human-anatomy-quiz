# Human Anatomy Quiz Game

## Introduction
The Human Anatomy Quiz is a simple, interactive Python terminal game designed to test a users knowledge of human anatomy. The game is structured into three main parts: the main menu, the instructions, and the quiz game itself.
It is aimed at individuals of all ages who are interested in learning about the human body in a fun and engaging way. The game can be useful to students learning Human Anatomy who want to test their knowledge.


### How to Play
- Answer a series of multiple-choice questions by typing the letter corresponding to your answer (a, b, c, or d), and then press Enter.
- After each question, the user will receive immediate feedback. If the user gets the answer right, the game will congratulate you. If the user gets it wrong, the game will provide the correct answer.
- The users score will be tallied as the user progresses through the quiz.


## Existing Features

### Welcome message 
The player is greeted with a welcome message and a Menu with a list of options.

### Input validation
- Players' responses to quiz questions are validated to ensure they select from the provided multiple-choice options (a, b, c, or d).

### Components
Structure: Each question is represented as a dictionary containing the question text, a list of options, and the correct answer identifier.
Fields:
question: A string containing the question to be asked.
options: A list of strings, each representing a possible answer. The options are labeled with letters (a, b, c, d) for easy reference.
answer: A string ('a', 'b', 'c', or 'd') indicating the correct answer to the question.


### Data Model Description
The Human Anatomy Quiz game is designed to test the player's knowledge of human anatomy through a series of multiple-choice questions. The game is structured into three main parts: the main menu, the instructions, and the quiz game itself. Below is a detailed breakdown of the data model and components used in the game.

### Components
1. Questions
Structure: Each question is represented as a dictionary containing the question text, a list of options, and the correct answer identifier.
Fields:
question: A string containing the question to be asked.
options: A list of strings, each representing a possible answer. The options are labeled with letters (a, b, c, d) for easy reference.
answer: A string ('a', 'b', 'c', or 'd') indicating the correct answer to the question.
2. Game Flow
The game flow is managed through a series of functions:

display_instructions(): Prints the game instructions to the console.
new_game(): Initiates a new game session, looping through the questions, collecting user responses, and scoring the game.
menu(): Displays the main menu and handles user input to navigate between playing the game, viewing instructions, or quitting.

### Game Logic
The game logic is encapsulated within the new_game() function, which iterates over the list of questions, displays each question with its options, and prompts the user for an answer.
The user's answer is compared against the correct answer specified in the question's data structure. The score is updated based on the correctness of the user's answers.
At the end of the quiz, the user's total score out of the number of questions is displayed.

### User Score
Calculation: The score is calculated by incrementing a counter each time the user selects the correct answer.
Display: At the end of a game session, the user's score is displayed, showing how many questions were answered correctly out of the total number of questions.


###  Feedback to the User
Upon answering a question, players receive immediate feedback:
- A correct answer results in a congratulatory message.
- An incorrect answer lets the user know it was incorrect and provides them with the correct answer helping to educate them.

### End of Game
Completing the quiz presents the user with a Game Over message followed by their score.

### Future Features
Expand the number of questions.


## Deployment Guide
This project has been successfully deployed through the Heroku platform, utilizing the Code Institute's Heroku mock terminal. To achieve this, the following deployment procedure was undertaken:

Repository Cloning: Initiated the process by cloning the project's repository to ensure a local copy for deployment preparation.

Heroku Application: Proceeded by establishing a new application within the Heroku environment, dedicated specifically to this project.

Buildpack Configuration: Configured the necessary buildpacks in a sequential order, starting with Python followed by Node.js, to accommodate the technology stack used in the project.

Environment Variables: Set up an essential configuration variable named PORT and assigned it the value 8000, which aligns with Heroku's required setup for web applications.

Repository Integration: Linked the Heroku application to this corresponding GitHub repository to enable direct deployments from the source code.

Application Deployment: Completed the deployment process by utilizing Heroku's 'Deploy' feature, which facilitated the transition of the project from development to a live environment.

The application is now live and can be accessed through Heroku's platform, ensuring users can interact with the Human Anatomy Quiz game in a fully functional terminal interface.