#village name:
#village size:
#population:
#resource:
#wich province:
#distric
#gn name






import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   


village_name = input("Enter your village name: ")
village_size = input("Enter your village size (sqft): ")
population = input("Enter your village population: ")
which_province = input("Enter the province  : ")
distric = input("Enter the distric: ")
girama_nilathari_name = input("Enter your village girama nilathari  name : ")
resources = input("Enter your village resources: ")




story = f'Hi, I am a story teller robot, today I am going to present the story village of {village_name}, this village has{village_size}.{village_name} have{population}population.{village_name}  is in profince of {which_province}. {village_name} is in distric of{distric}, {village_name} girama nilathari name is {girama_nilathari_name }. there are{resources}'

engine.say(story)
engine.runAndWait()