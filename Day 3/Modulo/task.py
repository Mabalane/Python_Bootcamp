print(10 % 3)

# task 2
print("check if your number is even or odd")
userInput= int(input("enter the Number you want to check if its odd or even\n"))
modula = userInput%2
if modula == 0:
    print(f"{userInput}, is an even number")
else:
    print(f"{userInput}, is an odd number")