import pyttsx3
engine = pyttsx3.init()



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   


name = input("enter your country  name: ")
current_president = input("enter your president: ")
religous_demography = input("enter your religous: ")
famous_tourist_places = input("enter your famous tourist: ")
population = input("enter your population: ")
srilanka_total_km = input("enter your country total km ")


story = f'Hi, I am a story teller robot, today I am going to present the story of {name}, {name}current president name is {current_president}.srilanka religous_demography is  {religous_demography} .there are many tourist places {famous_tourist_places}. and srilanka population is {population}. and srilanka total kilometers {srilanka_total_km}'

engine.say(story)
engine.runAndWait()