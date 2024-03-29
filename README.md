# Human Anatomy Quiz Game

## Introduction
The Human Anatomy Quiz is a simple, interactive Python terminal game designed to test a user's knowledge of human anatomy. The game is structured into four main parts: the main menu, the instructions, the top 10 leaderboard and the quiz game itself.
It is aimed at individuals of all ages who are interested in learning about human anatomy in a fun and engaging way. The game can be particularly useful to students learning human anatomy who want to test their knowledge or prepare for exams and have a fun and engaging experience.
[Click here for a live link of the quiz](https://human-anatomy-quiz-c547bec37202.herokuapp.com/)


### How to Play
- Answer a series of multiple-choice questions by typing the letter corresponding to your answer (a, b, c, or d), and then press Enter.
- After each question, the user will receive immediate feedback. If the player gets the answer right, the game will give feedback that you are correct. If the player gets the answer wrong, the game will provide feedback to the player that the answer was incorrect and then provide you with the correct answer.
- The users score will be tallied as the user progresses through the quiz.
- After completion of the quiz the score will be updated to a leaderboard of the top 10 scores.

### Target Users
This game is aimed at all individuals but mainly caters to students who are studying human physiology and anatomy. These students often need to test their knowledge as they prepare for exams. The quiz provides a valuable tool for them to assess their knowledge of anatomy and reinforce their learning through interactive gameplay. Many students preparing for exams, require resources to help them review and practice. This game offers a structured quiz format that covers essential topics in human anatomy, allowing students to assess their strengths and weaknesses in specific areas of study.
The game offers a fun and engaging way for students to learn. By presenting questions in a quiz format with multiple-choice answers, it encourages active participation and stimulates memory recall. The inclusion of a leaderboard adds a competitive element to the game, motivating students to strive for higher scores and outperform their fellow students.
The game's accessibility makes it suitable for a wide range of users, from beginner-level students to those with more advanced knowledge of human anatomy. The clear instructions and intuitive gameplay make it easy for users to dive into the quiz and start testing their knowledge immediately. By allowing users to compete for top scores on the leaderboard, the game promotes a sense of community.


## Existing Features

### Start
The program starts with an infinite loop which will continue until a valid username is entered by the user. Prompting the user with the input function: "Enter your username:" 

![image](https://github.com/010001000100000101000001/human-anatomy-quiz/assets/147556282/1a673d1a-fc18-4385-a130-455b3ec7575b)


The  .strip() method is used to remove any leading or trailing whitespace from the input. This ensures that usernames with unintentional spaces are handled properly. The code checks if the entered username is empty and gives feedback to the user:  "Invalid. Please enter a non-empty username." The input("Press Enter to continue..") is used to pause the execution until the user presses enter giving the user time to respond.


![image](https://github.com/010001000100000101000001/human-anatomy-quiz/assets/147556282/3f10e1ad-e31c-4953-a32a-323c61f8a611)

If the length of the username exceeds 20 characters, the user is informed that the username is invalid, and they're prompted to enter a username with a maximum character length of 20.


![image](https://github.com/010001000100000101000001/human-anatomy-quiz/assets/147556282/c022cbfd-1140-402c-af4a-975fac11d397)


The isalnum() method checks if the user inputs other than alphanumeric characters and if it is, it prints an error message:


![image](https://github.com/010001000100000101000001/human-anatomy-quiz/assets/147556282/c5122094-aec2-4f65-b894-689de996bde7)


### Welcome message 
If the entered username is valid, the function exits the loop and returns the valid username with a welcome message and the Menu with a list of options.


![image](https://github.com/010001000100000101000001/human-anatomy-quiz/assets/147556282/1391176a-047d-4525-8072-3024bf809079)



### Input validation
- Players' responses to quiz questions are validated to ensure they select from the provided multiple-choice options (a, b, c, or d).

  ![image](https://github.com/010001000100000101000001/human-anatomy-quiz/assets/147556282/bbecfa21-0ebc-4618-9c59-167d460f096e)



### Data Model Description
The Human Anatomy Quiz game is designed to test the player's knowledge of human anatomy through a series of multiple-choice questions. The game is structured into four main parts: the main menu, the instructions, the leaderboard and the quiz game itself. Below is a detailed breakdown of the data model and components used in the game.


**The game flow is managed through a series of functions:**
- clear(): Clears the terminal screen using system calls.
- display_instructions(): Prints out the instructions for playing the quiz.
- update_scoresheet(username, score): Updates the scoresheet with the provided username and score, keeping only the top 10 scores.
- new_game(username): Initiates a new game session by presenting a series of questions, evaluating user responses, and updating the score.
- menu(): Displays the main menu allowing the user to start a new game, view instructions, check the leaderboard, or quit the game.
- get_valid_username(): Prompts the user to enter a valid username, ensuring it's non-empty, alphanumeric, and within a 20 character length limit.
- display_leaderboard(): Displays the top 10 scores from the scoresheet.


### Components
Each question is represented as a dictionary containing the question text, a list of options, and the correct answer identifier.
A string containing the question to be asked.
A list of strings, each representing a possible answer. The options are labeled with letters (a, b, c, d) for easy reference.
A string ('a', 'b', 'c', or 'd') indicating the correct answer to the question.

### Game Logic
The game logic is encapsulated within the new_game() function, which iterates over the list of questions, displays each question with its options, and prompts the user for an answer.
The user's answer is compared against the correct answer specified in the question's data structure. The score is updated based on the correctness of the user's answers.
At the end of the quiz, the user's total score out of the number of questions is displayed.

### User Score
Calculation: The score is calculated by incrementing a counter each time the user selects the correct answer.
Display: At the end of a game session, the user's score is displayed, showing how many questions were answered correctly out of the total number of questions.

![image](https://github.com/010001000100000101000001/human-anatomy-quiz/assets/147556282/6ff48f84-09ef-4d03-957c-11d370370a2d)


### Google Sheets Integration
- **Score Tracking**: User scores are stored in a Google Sheets document named "human_anatomy_quiz". Each time a player completes  
   a game session, their username and score are added to the scoresheet.
- **Leaderboard Display**: The top 10 scores are displayed in the scoresheet, allowing players to see how they compare to others. 
  The scoresheet is updated dynamically as new scores are added.

  ![image](https://github.com/010001000100000101000001/human-anatomy-quiz/assets/147556282/9252415b-0f88-4877-bb8f-9bdbfba7f35d)



###  Feedback to the User
Upon answering a question, players receive immediate feedback:
- A correct answer results in a print statement that reads "Correct!" which is in bright green text that indicates to the user they choose the correct answer. This is achieved by importing the colorama module and applying the necessary changes to the code.

![image](https://github.com/010001000100000101000001/human-anatomy-quiz/assets/147556282/5240f0ef-0f28-402a-8015-9144b44e5ccb)

  
- An incorrect answer lets the user know it was incorrect and provides them with the correct answer helping to educate them. This is white text with a red background indicating that the answer was wrong also achieved using the imported colorama module. This was orginally in red text with a black background but the visibility of the text did not come across very clearly.

  ![image](https://github.com/010001000100000101000001/human-anatomy-quiz/assets/147556282/c6804e48-5561-45cb-8e5e-85eb86226142)


### End of Game
At the end of the quiz, the user receives a "Game Over" message along with their final score. Their score is then evaluated to determine if it qualifies for placement on the leaderboard.

If the user's score is high enough to enter the top 10 scores, it will be updated on the leaderboard. The script checks if the user's score is higher than the lowest score currently on the leaderboard. If it is, the lowest score is replaced with the user's score. Additionally, if the user's score is higher than all existing scores on the leaderboard, they will claim the number 1 position.

This process ensures that the leaderboard reflects the top scoring players, with the most recent high scores included.

![image](https://github.com/010001000100000101000001/human-anatomy-quiz/assets/147556282/e0290e6f-e6eb-429c-9375-3567df974040)



### Future Features
- **Expand the Number of Questions**: Introduce a larger pool of questions to keep the game challenging and engaging for players.
- **Timer**: Introduce a timer that marks the question as incorrect if the user does not answer in 10 seconds.
- **ASCII Art**: Add some fun ASCII Art to make the quiz more appealing.
- **Terminal-Based UI Libraries**: Import libraries like "curses or "blessed" to enhance the user experience.


## Testing
**- I tested my code using the Python linter provided by Code Institute, which checks for adherence to the PEP8 standard.**

| Description          | Expected Outcome                                                                 | Result                |
|----------------------|----------------------------------------------------------------------------------|-----------------------|
| User input validation | Prompts user to enter a username. If the username is not empty spaces and is within 20 characters and contains only letters and numbers it will return the username with a welcome message and the menu with the list of options.  |  Pass   |
| Incorrect input(1) | If the user inputs empty spaces it is handled by the code and returns a print statement "Invalid. Please enter a non-empty username." The user is prompted to press Enter to continue and the infinite loop repeats untill a valid username is entered. | Pass   |
| Incorrect input(2) | If the user inputs special characters it is handled by the code and returns a print statement "Invalid. Letters and numbers only." The user is prompted to press Enter to continue and the infinite loop repeats untill a valid username is entered. | Pass   |
| Incorrect input(3) | If the user inputs more than 20 characters it is handled by the code and returns a print statement "Invalid. Maximum character length is 20." The user is prompted to press Enter to continue and the infinite loop repeats untill a valid username is entered. | Pass   |
| Play Game | Game initialises when user selects "1. Play Game" the terminal is cleared and the first question is displayed. | Pass   |
| Display instructions | Instructions are displayed properly. The user can navigate back to the main menu from the instructions section. | Pass   |
| Display the leaderboard  | The top 10 scores is displayed on the leaderboard in the format "username: (score)" The leaderboard displays the scores in descending order. The leaderboard displays only the top 10 scores. The user can navigate back to the main menu from the leaderboard. |  Pass   |
| Answer input validation     | Answers are validated from the multiple choice options (a, b, c or d). If any other character, empty space or combination is input it is handled by the code and a print statement is returned. "Invalid answer, Try again!" This repeats an infinite loop until a valid answer is input. | Pass   |
| Answer questions     | Questions are presented, and user's answers are evaluated    | Pass   |
| Display final score  | Final score is displayed at the end of the game    | Pass   |
| Update leaderboard    | Scores are updated in the leaderboard section if the score makes it in the top 10   | Pass   |
| Quit Game    | Program stops running when the user chooses to quit    | Pass   |
| Main menu display | Main menu options are displayed correctly | Pass |
| Clear screen | Terminal screen is cleared before displaying new content |  Pass |
| Color formatting | Text is displayed with appropriate colors for emphasis | Pass |

### Integration Testing
| Description | Expected Outcome | Result |
|-------------|------------------|-------|
| Google Sheets integration | The program successfully writes and reads scores from Google Sheets | Pass |
| Authentication | Authentication with Google API succeeds | Pass |


## Deployment Guide
This project has been successfully deployed through the Heroku platform, utilizing the Code Institute's Heroku mock terminal. This is a link to my  To achieve this, the following deployment procedure was undertaken:

**Repository Cloning**: Initiated the process by cloning the project's repository to ensure a local copy for preparing deployment.

**Heroku Application**: Proceeded by establishing a new application within the Heroku environment, dedicated specifically to this project.

**Buildpack Configuration**: Configured the necessary buildpacks in a sequential order, starting with Python followed by Node.js, to accommodate the technology stack used in the project.

**Environment Variables**: Set up an essential configuration variable named PORT and assigned it the value 8000, which aligns with Heroku's required setup for web applications. Set up Google Sheets API credentials, to enable interaction with the Google Sheets document for score tracking.

**Repository Integration**: Linked the Heroku application to this corresponding GitHub repository to enable direct deployments from the source code.

**Application Deployment**: Completed the deployment process by utilizing Heroku's 'Deploy' feature, which facilitated the transition of the project from development to a live environment.

The application is now live and can be accessed on https://human-anatomy-quiz-c547bec37202.herokuapp.com/

## Google Cloud Platform Setup
To enable the integration with Google Sheets API, the following steps were taken on the Google Cloud Platform:
1. **Credentials Creation**: A Credentials file was created on the Google Cloud Platform to authenticate API requests from the 
Python application.
2. **API Activation**: Both Google Sheets API and Google Drive API were enabled for the project to allow access to Google Sheets
documents and manage files on Google Drive.
3. **Permissions Setup**: The service account "humananatomyquiz@human-anatomy-quiz-414515.iam.gserviceaccount.com" was granted 
editor access to the Google Sheets document to enable it to update scores.


## How to fork this repository
Click on the "Fork" button at the top right of the page and wait for a couple of seconds for the newly forked repository to be created under your GitHub account.

## Credits
The ability to set up Google sheets was taken from the series of videos on the love_sandwiches project. I used tutorials, guides and information from https://www.codecademy.com/, https://www.freecodecamp.org/, https://www.w3schools.com/, https://pypi.org/ and https://www.youtube.com/.

## Acknowledgements
**Special Thanks:**
Thank you to Code Institute and Matt Boden who provided me with the guidance to complete this project.
