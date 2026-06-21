# Python Knowledge Quiz Application

A dynamic, interactive desktop quiz application built with Python and Tkinter. This application allows users to either load pre-configured quiz questions from a JSON file or dynamically input questions manually through the command line before launching an interactive GUI.

---

## 📌 Table of Contents
* [Features](#-features)
* [Prerequisites](#-Prerequisites)
* [Setup & Usage Instruction](#-Setup_&_Usage_Instruction)
* [📝 Code Breakdown](#-code-breakdown)

---


##  Features

* **Dynamic Data Input Systems**
  * **File Processing Mode (`F`):** Automatically reads, validates, and parses structured question banks, option matrices, and solution indexes directly from a standalone JSON configuration file.
  * **Manual Terminal Mode (`M`):** Provides a robust, interactive Command Line Interface (CLI) wizard featuring continuous type-validation loops to ensure question counts, option strings, and correct key ranges conform to expected structures before launching the interface.

* **User Interface & Layout Engine**
  * Built using a responsive Tkinter grid matrix configuration to preserve layout formatting across varying screens.
  * Implements a custom color palette featuring deep burgundy primary headers (`#6E1D2E`), high-contrast modern typography (`Ariel`), and standardized spacing configurations.
  * Utilizes dynamic control variables (`tk.IntVar`) bound to a custom radio button matrix to automatically clear state, handle user input selections, and prevent duplicate data cross-contamination between questions.

* **Asynchronous Vector Animation Engine**
  * Features a custom vector-rendering system built directly onto a Tkinter `Canvas` layer widget.
  * Implements a non-blocking asynchronous animation loop using internal event-driven clock ticks (`self.gui.after()`).
  * Dynamically computes and updates shape coordinates on a transparent overlay mask to render a smooth, floating balloon visual reward (`fly_balloon`) upon processing correct answer flags.

* **State Tracking & Persistent Logging**
  * Manages real-time application state variables tracking internal index counters (`self.q_no`) and absolute accuracy metrics (`self.correct`).
  * Features built-in input interceptors that halt application workflows and display soft-warning dialog boxes if a user attempts to proceed without selecting an option.
  * Automatically calculates ultimate performance percentages and appends a clean, formatted plain-text analytics block to a local tracking repository (`quiz_results.txt`) upon quiz completion.
 

##  Prerequisites

To run this application, you only need **Python 3.x** installed. The application relies entirely on Python's built-in standard libraries, meaning **no third-party package installations (`pip install`) are required**.

* `tkinter` (GUI builder)
* `json` (Data parsing)
* `sys` (System configurations)

## Setup & Usage Instruction
1. Run the Script
Open your terminal or command prompt, navigate to the project directory
2. Choose Configuration Mode
Upon launching, the console will prompt you to choose how questions are ingested:

Press F: To load from a file. You can press Enter to default to data.json or type the path to your custom JSON file.

Press M: To input manually. Follow the command line prompts to specify the number of questions, question text, 4 individual options, and the matching correct index integer (1-4).

3. Take the Quiz
The Graphical User Interface will automatically display:

* Select an option and click Next.

* If you answer correctly, an animation triggers alongside a congratulatory popup.

* If you try to proceed without picking an answer, a warning popup will block progress.

* Click Quit at any time to abort the session safely.


```markdown
# 🐍 Python Knowledge Quiz Application

A dynamic, interactive desktop Quiz Application built using Python and the `tkinter` GUI framework. The application allows users to either load quiz data from an external JSON file or input custom questions manually through the terminal before launching a styled graphical interface to take the quiz. It features an animated reward mechanism and persistent result logging.

---

## 🚀 Features

* **Dual Data Input Modes:** * **File Mode (F):** Load structured questions, choices, and answers instantaneously from a `.json` configuration file.
  * **Manual Mode (M):** Build a custom quiz on-the-fly via interactive terminal prompts.
* **Intuitive GUI Design:** Clean layouts with custom font hierarchies, dynamic button states, and clear warning/information modal dialogues via `tkinter.messagebox`.
* **Balloon Animation:** A visual `tkinter.Canvas` animation that flies a celebratory balloon across the screen upon selecting a correct answer.
* **Persistent Score Logging:** Automatically appends final performance breakdowns (Total Questions, Final Score, and Score Percentage) into a local `quiz_results.txt` file for tracking progress.

---

## 🛠️ Project Structure

```text
├── quiz_app.py          # Main application source code
├── data.json            # Sample quiz data file (JSON format)
└── quiz_results.txt     # Generated log file tracking user performance

```

---

## 📋 Prerequisites

To run this application, you only need Python 3.x installed. The application relies entirely on Python's built-in standard libraries, meaning no third-party package installations (`pip install`) are required:

* `tkinter` (GUI builder)
* `json` (Data parsing)
* `sys` (System configurations)

---

## 💾 JSON Data Format

If you choose to load quiz questions using a file, your JSON file must adhere to the following structure. Save it as `data.json` in the same directory as the script:

```json
{
  "question": [
    "What is the correct extension of a Python file?",
    "Which keyword is used to create a function in Python?"
  ],
  "options": [
    [".py", ".python", ".pyt", ".pyxt"],
    ["function", "def", "fun", "class"]
  ],
  "answer": [1, 2]
}

```

> 💡 **Note:** The answer array maps directly to the 1-indexed placement of the correct choice (e.g., `1` for Option 1, `2` for Option 2).

---

## 🔧 Setup & Usage Instruction

### 1. Run the Script

Open your terminal or command prompt, navigate to the project directory, and execute:

```bash
python quiz_app.py

```

### 2. Choose Configuration Mode

Upon launching, the console will prompt you to choose how questions are ingested:

* **Press F:** To load from a file. You can press `Enter` to default to `data.json` or type the path to your custom JSON file.
* **Press M:** To input manually. Follow the command line prompts to specify the number of questions, question text, 4 individual options, and the matching correct index integer (1-4).

### 3. Take the Quiz

The Graphical User Interface will automatically display:

* Select an option and click **Next**.
* If you answer correctly, an animation triggers alongside a congratulatory popup.
* If you try to proceed without picking an answer, a warning popup will block progress.
* Click **Quit** at any time to abort the session safely.


---

## ⚙️ Key Methods Overview

| Method / Function | Module | Description |
| --- | --- | --- |
| `load_data_from_file(filename)` | Data Module | Safe parsing of JSON schemas with generic `FileNotFoundError` catch-blocks. |
| `get_manual_input()` | Data Module | Multi-layer input validation loops protecting arrays from type mismatches. |
| `log_results_to_file(...)` | Data Module | Handles file append streams (`a`) to preserve historical runtime logs. |
| `fly_balloon()` | QuizApp Class | Leverages recursive canvas object translation via `.after()` scheduling to construct a frame-by-frame balloon animation thread. |
| `next_btn()` | QuizApp Class | Validates selected items, manages state index increments, and manages execution of teardown/success workflows. |








