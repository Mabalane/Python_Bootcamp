print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:   # while still in the age and they have paid (since im billing them on age and the photo they need to be on the same indentations)
        bill +=5 #this adds to the bill
        print("Please pay $5.")
    elif age <= 18:
        bill += 7
        print("Please pay $7.")
    else:
        bill += 12
        print("Please pay $12.")

        ##indentation plays a big role in Python(the spacings to break up lines and functions
    print("Images taken while you are on your ride to Joy with us  are sold here \nFor only $3 you can capture this moment for ever")
    photo = bool(input("Do you want a photo for the ride ?(y-for Yes|n-for No)\n"))
    if photo == "y":
        bill+=3
        print(f"The total bill for the ride, with a Captured memory is ${bill}")
    else:
        print(f"The bill without a captured memory is : ${bill}") # The boolean might not be the best option for this
else:
    print("Sorry you have to grow taller before you can ride.")
