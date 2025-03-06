length = len("12345") # it cant take integers ,. note len is more like count function
print(length)
#Type checking
print(type("ABC"))
print(type(123))
print(type(4.1))
print(type(True))
print(type(123_456_678_987))

#Type conversion
print("Number of letters in your name is: " + str(len(input("Enter your name\n")))) #Note len produces integers and strings and integers cant mix so chage the data types in the same print to use the same data type