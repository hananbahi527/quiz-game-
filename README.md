# Python Knowledge Quiz Application

A dynamic, interactive desktop quiz application built with Python and Tkinter. This application allows users to either load pre-configured quiz questions from a JSON file or dynamically input questions manually through the command line before launching an interactive GUI.

---

## 📌 Table of Contents
* [🚀 Features](#-features)
* [📂 Project Structure & Setup](#-project-structure--setup)
  * [1. JSON Data Format (Optional)](#1-json-data-format-optional)
  * [2. How to Run](#2-how-to-run)
* [📊 Result Logging](#-result-logging)
* [📝 Code Breakdown](#-code-breakdown)

---

## 🚀 Features

* **Dual Data Input Modes:** * **File Mode (`F`):** Load structured questions, multiple-choice options, and answers directly from a JSON file.
  * **Manual Mode (`M`):** Input custom questions, four distinct choices, and the correct answer index directly via the CLI.
* **Interactive GUI:** A clean Tkinter interface featuring a customized color scheme, custom typography, radio buttons for input, and error handlings.
* **Animated Visual Feedback:** Features a custom Tkinter Canvas balloon animation (`fly_balloon`) that floats up whenever a user submits a correct answer.
* **Persistence & Logging:** Progress is validated live, and final quiz metrics are automatically calculated and appended to a local history log file (`quiz_results.txt`).

