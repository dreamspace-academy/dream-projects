usernameFromServer = ""
passwordFromServer = ""

with open(r"system-info/credentials.txt", encoding='UTF8') as f:
    contents = f.readlines()
    usernameData = contents[0].split("=")
    usernameFromServer = usernameData[1].strip()

    passwordData = contents[1].split("=")
    passwordFromServer = passwordData[1].strip()


usernameFromUser = input("Enter your username: ")
passwordFromUser = input("Enter your password: ")

if(usernameFromUser == usernameFromServer and passwordFromUser == passwordFromServer):
    action = input("Insert: press 1 \nSearch: press 2\n ")


else:
    print("you failed")
