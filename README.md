# Interactive Quiz Application

A dynamic, interactive desktop quiz application built with Python and Tkinter. This application allows users to either load pre-configured quiz questions from a JSON file or dynamically input questions manually through the command line before launching an interactive GUI.

---

##  Table of Contents
* [Features](#-features)
* [Prerequisites](#-Prerequisites)
* [Setup & Usage Instruction](#-Setup_&_Usage_Instruction)
* [Key Methods Overview](#-Key_Methods_Overview)

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




##  Setup & Usage Instruction

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

##  Key Methods Overview

| Method / Function | Module | Description |
| --- | --- | --- |
| `load_data_from_file(filename)` | Data Module | Safe parsing of JSON schemas with generic `FileNotFoundError` catch-blocks. |
| `get_manual_input()` | Data Module | Multi-layer input validation loops protecting arrays from type mismatches. |
| `log_results_to_file(...)` | Data Module | Handles file append streams (`a`) to preserve historical runtime logs. |
| `fly_balloon()` | QuizApp Class | Leverages recursive canvas object translation via `.after()` scheduling to construct a frame-by-frame balloon animation thread. |
| `next_btn()` | QuizApp Class | Validates selected items, manages state index increments, and manages execution of teardown/success workflows. |








