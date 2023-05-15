import tkinter as tk
from tkinter import *
import pyttsx3

engine=pyttsx3.init()
def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.sttop

root=Tk()
textv=StringVar()

obj=LabelFrame(root,text="Text to speach",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lbl=Label(obj,text="Text",font=30)
lbl.pack(side=tk.LEFT,padx=5)

Text=Entry(obj,textvariable=textv,font=30,width=25,bd=5)
Text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="speak",font=20,bg="black",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)


root.title("Text to speach")
root.geometry("500x200")
root.resizable(False,False)
root.mainloop()