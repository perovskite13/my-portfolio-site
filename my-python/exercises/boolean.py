moths_in_house = input("is there moths in the house? True or False: ")
mitch_is_home = input("is mitch home? True or False: ")

# Q1
if moths_in_house == "True":
    print("Get the moths!")

if moths_in_house == "False":
    print("no threats detected.")

#Q2
if moths_in_house == "True" and mitch_is_home == "True":
    print("Hooman! Help me get the moths!")
elif moths_in_house == "False" and mitch_is_home == "False":
    print("No threats detected.")
elif moths_in_house == "True" and mitch_is_home == "False":
    print("Meoooooow! Hiss!")
elif moths_in_house == "False" and mitch_is_home == "True":
    print("Climb on Mitch.")

#Q3
light_colour = input("Hi! I'm a Red Light Camera! when I turn [color]:")
car_detected = input(" or when I detect a car [True or False]: ")

if light_colour == "Red" and car_detected == "False":
    print("Do nothing.")
elif light_colour == "Red" and car_detected == "True":
    print("Flash!")
elif light_colour == "Green" and car_detected == "False":
    print("Do nothing.")
elif light_colour == "Green" and car_detected == "True":
    print("Do nothing.")
elif light_colour == "Amber" and car_detected == "False":
    print("Do nothing.")
elif light_colour == "Amber" and car_detected == "True":
    print("Do nothing.")

#Q4
n = int(input("Hi! I'm a robot that decide whether you can ride rollercoaster or not. Tell me... how tall are you?: "))

if n >= 120:
    print(f"So... you are {n} cm tall... I guess you could Hop on!")
elif n < 120:
    print(f"So... you are {n} cm tall... Sorry, not today :(")
