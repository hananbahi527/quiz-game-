#  Python Knowledge Quiz Application

A dynamic, interactive desktop Quiz Application built using Python and the `tkinter` GUI framework. The application allows users to either load quiz data from an external JSON file or input custom questions manually through the terminal before launching a styled graphical interface to take the quiz. It features an animated reward mechanism and persistent result logging.

---

##  Features

* **Dual Data Input Modes:** * **File Mode (F):** Load structured questions, choices, and answers instantaneously from a `.json` configuration file.
  * **Manual Mode (M):** Build a custom quiz on-the-fly via interactive terminal prompts.
* **Intuitive GUI Design:** Clean layouts with custom font hierarchies, dynamic button states, and clear warning/information modal dialogues via `tkinter.messagebox`.
* **Balloon Animation:** A visual `tkinter.Canvas` animation that flies a celebratory balloon across the screen upon selecting a correct answer.
* **Persistent Score Logging:** Automatically appends final performance breakdowns (Total Questions, Final Score, and Score Percentage) into a local `quiz_results.txt` file for tracking progress.

---

##  Project Structure

```text
├── quiz_app.py          # Main application source code
├── data.json            # Sample quiz data file (JSON format)
└── quiz_results.txt     # Generated log file tracking user performance
