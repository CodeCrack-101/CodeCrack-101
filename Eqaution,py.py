from tkinter import *
from tkinter import messagebox

def Solve():
    equation = entry.get()
    try:
        numbers = list(map(float, equation.split(',')))
        average = sum(numbers) / len(numbers)
        messagebox.showinfo("Solution", f"The average is: {average}")
    except Exception as e:
        messagebox.showerror("Error", "Please enter numbers separated by commas.")

root = Tk()
root.geometry("780x300")
root.config(bg="red")

Label(root, text="Enter Numbers Separated By Comma's", fg="black", bg="red", font=("Arial", 14)).place(x=50, y=50)
entry = Entry(root, width=50)
entry.place(x=400, y=55)

Button(root, text="Solve", fg="black", command=Solve, width=20).place(x=480, y=100)

root.mainloop()
