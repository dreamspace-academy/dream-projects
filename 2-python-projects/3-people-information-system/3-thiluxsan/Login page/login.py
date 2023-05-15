from tkinter import *
from PIL import ImageTk

#Functionality Part

def on_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

    





              #GUI Part
login_window=Tk()
login_window.geometry('1024x768+100+20')
login_window.resizable(0,0)
bgImage=ImageTk.PhotoImage(file='page.jpg')

    
   





bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)
login_window.title('Login Page')







heading=Label(login_window,text='USER LOGIN',font=('Helvetica',18,'bold'),bg='coral',fg='white')
heading.place(x=660,y=160)




usernameEntry=Entry(login_window,width=30,font=('Helvetica',11,'bold'),bd=0,fg='black')
usernameEntry.place(x=620,y=250)
usernameEntry.insert(0,'user name')

usernameEntry.bind('<FocusIn>',on_enter)





passwordEntry=Entry(login_window,width=30,font=('Helvetica',11,'bold'),bd=0,fg='black')
passwordEntry.place(x=620,y=300)
passwordEntry.insert(0,'password')

passwordEntry.bind('<FocusIn>',on_enter)




login_window.mainloop()


