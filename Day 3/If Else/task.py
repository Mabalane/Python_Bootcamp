print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
min_height = 175
if height < min_height:
    print("Sorry your height doesnt allow for this ride")
else:
    print("You are eligible to ride")