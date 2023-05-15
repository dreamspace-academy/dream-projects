from tkinter import *


def save_info():
  user_info = username.get()
  pass_info = password.get()

  print(user_info, pass_info, )
  id = input("Enter ID: ")
  file = open(f"{id}.txt", "w")


  #file = open("credentials.txt", "w")
  file.write(user_info + "\n")
  file.write(pass_info + "\n")
  
  file.close()
  print(" User ", user_info, " has been registered successfully")

  user_entry.delete(0, END)
  pass_entry.delete(0, END)
 
  
screen = Tk()
screen.geometry("300x300")
screen.title("User Form")
heading = Label(text = "User Details", bg = "red", fg = "black", width = "400", height = "2")
heading.pack()
 
user_text = Label(text = "Username * ",)
pass_text = Label(text = "Password * ",)

user_text.place(x = 15, y = 70)
pass_text.place(x = 15, y = 140)



username = StringVar()
password = StringVar()

user_entry = Entry(textvariable = username, width = "30")
pass_entry = Entry(textvariable = password, width = "30")


user_entry.place(x = 15, y = 100)
pass_entry.place(x = 15, y = 180)


register = Button(screen,text = "Register", width = "30", height = "2", command = save_info, bg = "aqua")
register.place(x = 15, y = 250)

root = Tk()
root.mainloop()

while(True):
  END
