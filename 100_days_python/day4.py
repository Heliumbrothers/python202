import random

random_integer = random.randint(1, 2)
if random_integer == 1:
  print("Tails")
  
else:
  print("Heads")



name_string = (" ")

import random
names = name_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
name_picked = random.randint(0,len(names))
print(f'{names[name_picked]} is going to buy the meal today!')




line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0]







