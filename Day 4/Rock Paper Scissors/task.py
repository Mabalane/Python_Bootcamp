import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#try using numbers to determin whats in the list and thus use operators to make the code short
opponent = random.randint(0,2)
player = input("which do you choose, rock, paper or scissors\n").lower()
game = ["rock","paper","scissors"]
result = (game[opponent])
if result=="rock" and player=="rock":
    print("This is a draw")
    print(f"you have chosen {player} \n:{rock}")
    print(f"The computer has also chosen {result} \n:{rock}")
elif result =="rock" and player=="paper":
    print("You have Won this round , Congratulations")
    print(f"you have chosen {player} \n:{paper}")
    print(f"The computer has also chosen {result}\n :{rock}")
elif result=="rock" and player=="scissors" :
    print("Sorry, You have lost this round!")
    print(f"you have chosen {player}\n :{scissors}")
    print(f"The computer has chosen {result} \n:{rock}")

elif result =="paper" and player=="rock":
    print("Sorry, You have lost this round!")
    print(f"you have chosen {player} \n:{rock}")
    print(f"The computer has chosen {result}\n :{paper}")
elif result=="paper" and player=="scissors" :
    print("You have Won this round , Congratulations")
    print(f"you have chosen {player}\n :{scissors}")
    print(f"The computer has chosen {result} \n:{paper}")
elif result == "paper" and player == "paper":
    print("This is a draw")
    print(f"you have chosen {player}\n :{paper}")
    print(f"The computer has also chosen {result}\n :{paper}")

elif result == "scissors" and player == "rock":
    print("Sorry, You have lost this round!")
    print(f"you have chosen {player} \n:{rock}")
    print(f"The computer has chosen {result} \n:{scissors}")
elif result == "scissors" and player == "paper":
    print("You have Won this round , Congratulations")
    print(f"you have chosen {player} \n:{paper}")
    print(f"The computer has chosen {result}\n :{scissors}")
elif result == "scissors" and player == "scissors":
    print("Sorry, You have lost this round!")
    print(f"you have chosen {player}\n :{scissors}")
    print(f"The computer has also chosen {result}\n :{scissors}")