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
    engine_displacement = input("Enter your engine CC: ")
    number_of_cylender = input("Enter howmany cylender/s in your car: ")
    max_power = input("Enter your car's maximum power:  ")
    seating_capacity = input("Enter your car's seating capacity: ")
    transmission_type = input("Enter your Transmission type: ")
    fuel_tank_capacity = input("Enter your fuel tank capacity: ")
    other_featuers = input("Enter about your car's other special abilities: ")


else:
    exit()




engine.say(story)
engine.runAndWait()