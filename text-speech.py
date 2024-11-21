import tkinter as tk
from tkinter import *
import pyttsx3

root = Tk()

root.geometry("700x400")
root.title("Text To Speech")

def speak():
    engine = pyttsx3.init()
    engine.say(ent.get())
    engine.runAndWait()
    engine.stop()
    
txt = Label(root, text="Text To Speech",justify="center", fg="black", font=("Arial", 30))
txt.place(x=190,y=50)

ent = Entry(root,width=50)
ent.place(x=180,y=110)
ent.focus()

txt = Button(root, text="Speak", fg="White",bg="black", font=("Arial",15),command=speak)
txt.place(x=280,y=150)
   
root.mainloop()
