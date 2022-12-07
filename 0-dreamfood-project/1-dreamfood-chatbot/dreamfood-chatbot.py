import os
import pyttsx3
from playsound import playsound
import webbrowser

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   


def talk_function(message):
    print(f'dreamfood: {message}')
    engine.say(message)
    engine.runAndWait()


while True:
    userInput = input("You: ")
    userInput = userInput.lower()

    if userInput == "hi":
        talk_function("hello")

    elif userInput == 'do you have vegetarian':
        talk_function('yes we have')

    elif userInput == 'do you have kids menu':
        talk_function('yes we have. please type kids menu')


    elif userInput == "do you have vegan":
        talk_function("yes we have")

    elif userInput ==  "at what time you open":
        talk_function("daily six thirty AM to ten thirty PM")

    elif userInput == "do you have beverages":
        talk_function("yes we have")

    elif userInput == "is any family packages available":
        talk_function("yes we have some packages.please type packages")

    elif userInput == 'do you have kids menu':
        talk_function('yes we have.please type kids menu')

    elif userInput == "open youtube":
        webbrowser.open('http://www.youtube.com')
    
    elif userInput == "can i have your menu":
        os.startfile("menu.jpg")

    elif userInput == "kids menu":
        os.startfile("kids menu.jpg")
    
    elif userInput == "packages":
        os.startfile("package menu.jpg")

    elif userInput == "open your website":
        os.startfile("file:///C:/Users/Aninilavan/Desktop/dream-projects/0-dreamfood-project/0-dreamfood-website/index.html")

    elif userInput == "open dreamfood":
        os.startfile("file:///C:/Users/Aninilavan/Desktop/dream-projects/0-dreamfood-project/0-dreamfood-website/index.html")


        