bmi = 84 / 1.65 ** 2
print(bmi) # i want to round it up
print(round(bmi)) # rounding whole number rounding

#grounding
print(str(bmi))

#how can i choose to which decimal places do i need
print(round(bmi,2))
 #f-string- its there to help with the type casting where you have to convert things to string . it converts for you
 #Here is how it works
age = 12
print(f"I am {age} years old") #Converted the int into string
#the use of assignment operators
score = 0
score +=2  #It changed the value of score / manipulating a value based on its recent value.
print(score)