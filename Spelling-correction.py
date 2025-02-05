import tkinter as tk
from textblob import TextBlob
root = tk.Tk()
root.geometry("700x400")
root.config(background="#949fa8")
root.title("Spelling Checker")

# Function to check spelling
def checking():
    word = text_entry.get()
    if word.strip():  
        a = TextBlob(word)
        corrected_text = str(a.correct())
        result_label.config(text=f"Correct Text Is: {corrected_text}")
    else:
        result_label.config(text="Please Enter Some Text...")


heading = tk.Label(root,text="Spelling Checker",font=("Trebuchet MS", 30, "bold"),fg="#616466",bg="#949fa8")
heading.pack(pady="50px")

text_entry = tk.Entry(root, justify="center", width=30, border=4, font=("Arial", 14))
text_entry.place(x=180,y=150)
text_entry.focus()

check_button = tk.Button(root, text="Check",bg="#474745",fg="white", font=("Trebuchet MS", 15, "bold"),command=checking)
check_button.pack()


result_label = tk.Label(root,text="", font=("Trebuchet MS", 20, "bold"),fg="#616466",bg="#949fa8")
result_label.place(x=50, y=280)


root.mainloop()
