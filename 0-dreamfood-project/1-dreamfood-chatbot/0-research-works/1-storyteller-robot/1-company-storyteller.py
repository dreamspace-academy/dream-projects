#company name
#company location
#company details
#company mission and vision
#company staff




import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   


company_name = input("Enter your company name: ")
company_location = input("Enter your company location: ")
company_field = input("What's your company based on: ")
company_mission = input("Enter your company mission and vision: ")
companystaff = input("How many employees works in your company: ")






story = f'Hi, I am a story teller robot, today I am going to present the story of {company_name}, {company_name} is in {company_location}. this is a {company_field} there are{companystaff} works in this company and {company_name} mission and vision{company_mission}'

engine.say(story)
engine.runAndWait()