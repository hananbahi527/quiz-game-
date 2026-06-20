# Python Knowledge Quiz Application

A dynamic, interactive desktop quiz application built with Python and Tkinter. This application allows users to either load pre-configured quiz questions from a JSON file or dynamically input questions manually through the command line before launching an interactive GUI.

---

## Table of Contents
* [ Features](#-features)
* [ Requirements](#️-requirements)
* [ Project Structure & Setup](#-project-structure--setup)
  * [1. JSON Data Format (Optional)](#1-json-data-format-optional)
  * [2. How to Run](#2-how-to-run)
* [ Result Logging](#-result-logging)
* [ Code Breakdown](#-code-breakdown)

---

##  Features

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
---

##  Requirements

* **Python 3.x**
* **Tkinter** (usually comes pre-installed with standard Python distributions)

---

## Project Structure & Setup

### 1. JSON Data Format (Optional)
If you prefer loading questions via a file, create a file named `data.json` in the root directory of the project using the following structure:

```json
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
