import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_selection = random.randint(0,4)
print(friends[random_selection]) #this is one way to get the random value in the list

#alternatively
print(random.choice(friends))