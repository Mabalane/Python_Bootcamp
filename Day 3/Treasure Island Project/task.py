from queue import PriorityQueue

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n You are in a forest and reach a 2 way.\n Which way do you turn")
choice1=input("Enter Left or Right")
if choice1 == "left" or "Left":
    print("Good choice , this turned out to be a safe route to take.\n It starts raining and you encounter an over flowing river\nWhat do you do?  ")
    choice2 = input('Wait the rain out or Swim across the river, "wait" / "swim"') # take note on how this is done
    if choice2 == "wait" or "Wait":
        print("That's a great move, now the sun is out and you made it over the river\n You encounter 3 tree houses with different colors, which do you pick ")
        choice3 = input("The Yellow,Red or Blue coloured tree houses").lower() #the .lower helps us get the unswer in lover cases(google more on these)
        if choice3 == "Yellow" or "yellow" or "YELLOW":  #IS THERE A SHORTER WAY TO GET CAPITAL AND LOWER CASE THINGS
            print("Well done!, you have found your treasure")
        elif choice3== "Red" or "red" or "RED":
            print("The red tree house is filled with distractions, music, Good company and food.\nYou end up forgetting about the treasure.")
        elif choice3=="Blue" or "blue" or "BLUE" :
            print("you get locked inside and die of hunger")
        else:
            print("you get a sickness and die")
    else:
        print("As you are swimming across the water level rises because of the rain and the current pulls you to deathly water fall. Game over!")
else:
    print("This is wrong turn, you encounter barbarians that eat people and you are tonight's feast")


