import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

vehicle_type = input("Enter your vehicle type: ")

vehicle = " "



if vehicle_type == "car":

    vehicle_model_name = input("Enter your vehicle model name: ")
    averege_mileage = input("Enter your average mileage: ")
    city_mileage = input("Enter your city mileage: ")
    fuel_type = input ("Enter your fuel type:")
    engine_displacement = ("Enter your engine CC: ")
    number_of_cylender = ("Enter howmany cylender/s in your car: ")
    max_power = ("Enter your car's maximum power:  ")
    seating_capacity = ("Enter your car's seating capacity: ")
    transmission_type = ("Enter your Transmission type: ")
    fuel_tank_capacity = ("Enter your fuel tank capacity: ")
    other_featuers = ("Enter about your car's other special abilities: ")


else:
    exit()







story = f'Hi, I am a story teller AI, today I am going to present the story of {name}, {name} is from {nationality}. {genderPronuon} is {age} years old. {genderPronuon} is working as a {job}, {genderPronuon2} free time actitivies are {activities}'

engine.say(story)
engine.runAndWait()