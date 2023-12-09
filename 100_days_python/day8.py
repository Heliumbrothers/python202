name = str(input("what is your name?\n"))
location = str(input("where do you live?\n"))


def greet_with(name, location):
    print("\n\n\n")
    print(f"hello {name}")
    print(f"what is it like in {location}?")


greet_with(name, location)




# Write your code below this line 👇
import math



# Write your code above this line 👆

# Define a function called paint_calc() so the code below works.   


def paint_calc(height, width, cover):
  number_of_cans = (height * width) / cover
  return math.ceil(number_of_cans)


# 🚨 Don't change the code below 👇


test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
print(f'You\'ll need {paint_calc(height=test_h, width=test_w, cover=coverage)} cans of paint.')



# Write your code below this line 👇

def prime_checker(number):
  prime_number_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
  if number%2 == 0:
    print("It's not a prime number.")
  else:
    if number%3 == 0:
      print("It's not a prime number.")
    else:
      if number%5 == 0:
        print("It's not a prime number.")
      else:
        if number%7 == 0:
          print("It's not a prime number.")
        else:
          print("It's a prime number.")


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)