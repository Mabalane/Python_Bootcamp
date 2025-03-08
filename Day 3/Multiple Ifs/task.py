print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill +=5 #this adds to the bill
        print("Please pay $5.")
    elif age <= 18:
        bill += 5
        print("Please pay $7.")
    else:
        bill += 5
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
