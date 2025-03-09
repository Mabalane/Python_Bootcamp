import random

#this is to bring random things in the mix

randomnr = random.random() * 10# generates a random number from 0 to 1 , random float, inclusive and non-inclusive
print(randomnr)
rn = random.uniform(1,10) # the one can be inclusive of upper bound unlike random.random.

print(rn)
#python is a modular thing
#Heads or tails
randomToss = random.randint(0,1)
if randomToss==0:
    print("Heads")
else:
    print("Tails")