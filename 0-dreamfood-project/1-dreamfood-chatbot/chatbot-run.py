import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   


def talk_function(message):
    print(f'Computer: {message}')
    engine.say(message)
    engine.runAndWait()


while True:
    userInput = input("You: ")
    userInput = userInput.lower()

    if userInput == "hi":
        talk_function("Hello")

    elif userInput == "how are you?":
        talk_function("I am fine")



    

