bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill+=small_pizza
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y": #NESTED BECAUSE EXECUTES ONLY IF THE FIRST IF IS TRUE
        bill += 2
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese=="Y":
        bill+=1
elif size == "M":
    bill+=medium_pizza
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 3
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill+=large_pizza
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 3
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == "Y":
        bill += 1
print(f"Your final bill is: ${bill}.")



