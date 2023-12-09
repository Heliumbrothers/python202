import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many characters would you like in your password?\n")) 


password = [0]

for x in range(0, nr_letters-1):
    character_type = random.randint(1, 3)
    if character_type == 1:
        password.append (letters[random.randint(0, 25)])
    if character_type == 2:
        password.append(random.choice(numbers))
    if character_type == 3:
        password.append(random.choice(symbols))


print("your password could be" + str(password))
    



