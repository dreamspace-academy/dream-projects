import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   


name = input("Enter your name: ")
age = input("Enter your age: ")
job = input("Enter your job: ")
nationality = input("Enter your nationality: ")
activities = input("Enter your free time activities: ")
gender = input("Enter your gender: ")

genderPronuon = ""
genderPronuon2 = ""

if gender == "male":
    genderPronuon = "he"
    genderPronuon2 = "his"
elif gender == "female":
    genderPronuon = "she"
    genderPronuon2 = "her"



story = f'Hi, I am a story teller robot, today I am going to present the story of {name}, {name} is from {nationality}. {genderPronuon} is {age} years old. {genderPronuon} is working as a {job}, {genderPronuon2} free time actitivies are {activities}'

engine.say(story)
engine.runAndWait()