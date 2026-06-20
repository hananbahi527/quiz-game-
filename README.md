Here is the updated README.md with a clean, clickable Table of Contents added to make navigation seamless.

Python Knowledge Quiz Application
A dynamic, interactive desktop quiz application built with Python and Tkinter. This application allows users to either load pre-configured quiz questions from a JSON file or dynamically input questions manually through the command line before launching an interactive GUI.

 Table of Contents
 Features

 Requirements

 Project Structure & Setup

1. JSON Data Format (Optional)

2. How to Run

 Result Logging

 Code Breakdown

 Features
Dual Data Input Modes: * File Mode (F): Load structured questions, multiple-choice options, and answers directly from a JSON file.

Manual Mode (M): Input custom questions, four distinct choices, and the correct answer index directly via the CLI.

Interactive GUI: A clean Tkinter interface featuring a customized color scheme, custom typography, radio buttons for input, and error handlings.

Animated Visual Feedback: Features a custom Tkinter Canvas balloon animation (fly_balloon) that floats up whenever a user submits a correct answer.

Persistence & Logging: Progress is validated live, and final quiz metrics are automatically calculated and appended to a local history log file (quiz_results.txt).

Requirements
Python 3.x

Tkinter (usually comes pre-installed with standard Python distributions)

 Project Structure & Setup
1. JSON Data Format (Optional)
If you prefer loading questions via a file, create a file named data.json in the root directory of the project using the following structure:

JSON
{
  "question": [
    "What is the correct extension of a Python file?",
    "Which keyword is used to create a function in Python?"
  ],
  "options": [
    [".py", ".pyt", ".pt", ".pyw"],
    ["fun", "function", "def", "define"]
  ],
  "answer": [1, 3]
}
Note: The answer array contains the index of the correct option (ranging from 1 to 4).

2. How to Run
Clone or download the script file.

Open your terminal or command prompt, navigate to the project directory, and execute:

Bash
python quiz_app.py
Follow the CLI prompt to select your preferred input mode:

Enter F to load your data.json file.

Enter M to manually build a quiz session on the fly.

 Result Logging
Upon completion of the quiz, the application generates or appends data to a file named quiz_results.txt in the following format:

Plaintext
----------
Quiz Finished
Total: 2
Score: 2
Percentage: 100%
 Code Breakdown
load_data_from_file() / get_manual_input(): Modules tasked with parsing, structuring, and sanitizing the source questions dataset.

QuizApp Class: Manages the application workflow, state tracking (self.q_no, self.correct), rendering layout matrices, and coordinating component actions.

fly_balloon(): Utilizes Tkinter's internal clock loops (after()) to asynchronously manipulate coordinates of vector geometric elements on a layer mask for UI animation.
