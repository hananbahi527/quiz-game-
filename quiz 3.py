import tkinter as tk
from tkinter import messagebox as mb
import json
import sys

#DATA MODULES 
def load_data_from_file(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data['question'], data['options'], data['answer']
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        sys.exit()

def get_manual_input():
    print("\nManual Quiz Entry ")
    
    while True:
        try:
            num = int(input("How many questions do you want to add? "))
            if num > 0: break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    questions = []
    options = []
    answers = []

    for i in range(num):
        print(f"\nQuestion {i+1}")
        questions.append(input(f"Enter question {i+1}: "))
        
        opts = []
        for j in range(4):
            opts.append(input(f"   Option {j+1}: "))
        options.append(opts)
        
        while True:
            try:
                ans = int(input("Enter correct option number (1-4): "))
                if 1 <= ans <= 4:
                    answers.append(ans)
                    break
                print("   Out of range! Enter 1, 2, 3, or 4.")
            except ValueError:
                print("Numeric input required.")

    return questions, options, answers

def log_results_to_file(score, total, filename="quiz_results.txt"):
    percentage = int(score/total*100) if total > 0 else 0
    output_text = f"Quiz Finished\nTotal: {total}\nScore: {score}\nPercentage: {percentage}%"
    
    # Save to File
    with open(filename, "a") as f:
        f.write("\n" + "-"*10 + "\n" + output_text + "\n")

#GUI Class
class QuizApp:
    def __init__(self, questions, options, answers):
        self.gui = tk.Tk()
        self.gui.geometry("800x450")
        self.gui.title("Python Knowledge Quiz")
        self.questions = questions
        self.options = options
        self.answers = answers
        self.q_no = 0
        self.correct = 0
        self.opt_selected = tk.IntVar()
        self.display_title()
        self.question_label = self.display_question()
        self.radio_btns = self.create_radio_buttons()
        self.display_options()
        self.create_buttons()
        self.gui.mainloop()
    ٍٍ    
    def display_title(self):
        title = tk.Label(self.gui, text="QUIZ APPLICATION", width=50, 
                         bg="#6E1D2E", fg="white", font=("ariel", 20, "bold"))
        title.grid(row=0, column=0, columnspan=3, sticky="ew")

    def display_question(self):
        lbl = tk.Label(self.gui, text=self.questions[self.q_no], width=60,
                       font=('ariel', 16, 'bold'), anchor='w')
        lbl.grid(row=1, column=0, columnspan=3, padx=20, pady=20, sticky="w")
        return lbl

    def fly_balloon(self):
        canvas = tk.Canvas(self.gui, width=800, height=500, highlightthickness=0, bg=self.gui.cget("bg"))
        canvas.place(x=0, y=0)
        
        balloon = canvas.create_oval(375, 500, 425, 560, fill="red", outline="white")
        line = canvas.create_line(400, 560, 400, 580, fill="black")

        def animate():
            canvas.move(balloon, 0, -10)
            canvas.move(line, 0, -10)
            pos = canvas.coords(balloon)
            if pos[1] > -60:
                self.gui.after(20, animate)
            else:
                canvas.destroy() 

        animate()
    def create_radio_buttons(self):
        btns = []
        for i in range(4):
            btn = tk.Radiobutton(self.gui, text=" ", variable=self.opt_selected,
                                 value=i+1, font=("ariel", 14))
            btns.append(btn)
            btn.grid(row=2+i, column=0, columnspan=3, sticky="w", padx=50)
        return btns

    def display_options(self):
        self.opt_selected.set(0)
        for i, option in enumerate(self.options[self.q_no]):
            self.radio_btns[i]['text'] = option

    def check_ans(self):
     if self.opt_selected.get() == self.answers[self.q_no]:
        return True
     else:
        return False
    def next_btn(self):
        if self.opt_selected.get() == 0:
            mb.showwarning("Warning", "Please select an option first!")
            return
        if self.check_ans():
          self.correct += 1
          self.fly_balloon()
          mb.showinfo("Correct!", "Congratulations! Correct Answer 🎈")
        else:
            mb.showerror("Wrong", "Wrong Answer!")
        self.q_no += 1
        if self.q_no == len(self.questions):
            log_results_to_file(self.correct, len(self.questions))
            percentage = int(self.correct/len(self.questions)*100) if len(self.questions) > 0 else 0
            mb.showinfo("Final Score", f"Score: {percentage}%")
            self.gui.destroy()
        else:
            self.question_label.config(text=self.questions[self.q_no])
            self.display_options()

    def create_buttons(self):
        next_b = tk.Button(self.gui, text="Next", command=self.next_btn,
                           width=10, bg="#6E1D2E", fg="#FFFFFF", font=("ariel", 16, "bold"))
        next_b.grid(row=6, column=0, columnspan=3, pady=30) 
        
        quit_b = tk.Button(self.gui, text="Quit", command=self.gui.destroy,
                           width=7, bg="white", fg="#6E1D2E", font=("ariel", 16, "bold"))
        quit_b.grid(row=7, column=2, sticky="se", padx=60, pady=20)

if __name__ == "__main__":
    print("Welcome to the Quiz System")
while True:
    mode = input("Load from file (F) or enter manually (M)? ").strip().upper()
    
    if mode == 'F':
        path = input("Enter json filename (default 'data.json'): ") or "data.json"
        questions, options, answers = load_data_from_file(path)
        break
        
    elif mode == 'M':
        questions, options, answers = get_manual_input()
        break
        
    else:
        print("Invalid input! Please enter 'F' or 'M' only.")
QuizApp(questions, options, answers)
