import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

phone_type = input("Enter your phone model: ")
relesed_year = input("Enter your phone relesed year: ")
battery_capacity = input("Enetr your phone bettery capacity: ")
ram_capacity = input("Enter your phone ram capacity: ")
operatingsystem = input("Enter your phone operating system: ")
price = input("Enter your phone price: ")

story = f'Hi, I am a story teller robot, today I am going to present the story of{phone_type},it was relesed{relesed_year},it is condain{battery_capacity}capasity battery,it is  using {ram_capacity}random access memory,the phone is powerd by{operatingsystem},it is just{price}LKR.'
engine.say(story)
engine.runAndWait()
