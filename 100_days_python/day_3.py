# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
  print('This is an even number.')
else:
  print('This is an odd number.')








  # Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_as_float= float(height)
weight_as_int = int(weight)
bmi = weight_as_int / height_as_float**2

#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Equal to or over 25 but below 30 they are slightly overweight
#Equal to or over 30 but below 35 they are obese
#Equal to or over 35 they are clinically obese

if bmi <18.5:
  print(f'Your BMI is {bmi}, you are underweight.')
elif bmi < 25:
  print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi < 30:
  print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi < 35:
  print(f'Your BMI is {bmi}, you are obese.')
else:
  print(f'Your BMI is {bmi}, you are clinically obese.')









  import sys
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year%4 == 0:
  print("Leap year")
else:
  if year%100 > 0:
    if year%400 > 0:
      print("Not leap year")
    else:print("Leap year")
      
  else:("Leap year")








  print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N  
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
total_price = 0
if size == 'S':
  total_price += 15
  if add_pepperoni == 'Y':
    total_price += 2
    if extra_cheese == 'Y':
      total_price += 1
      print(f'Your final bill is: ${total_price}.')
    else:
      print(f'Your final bill is: ${total_price}.')
  elif extra_cheese == 'Y':
    total_price += 1
    print(f'Your final bill is: ${total_price}.')
  else:
    print(f'Your final bill is: ${total_price}.')

if size == 'M':
  total_price += 20
  if add_pepperoni == 'Y':
    total_price += 3
    if extra_cheese == 'Y':
      total_price += 1
      print(f'Your final bill is: ${total_price}.')
    else:
      print(f'Your final bill is: ${total_price}.')
  elif extra_cheese == 'Y':
    total_price += 1
    print(f'Your final bill is: ${total_price}.')
  else:
    print(f'Your final bill is: ${total_price}.')

if size == 'L':
  total_price += 25
  if add_pepperoni == 'Y':
    total_price += 3
    if extra_cheese == 'Y':
      total_price += 1
      print(f'Your final bill is: ${total_price}.')
    else:
      print(f'Your final bill is: ${total_price}.')
  elif extra_cheese == 'Y':
    total_price += 1
    print(f'Your final bill is: ${total_price}.')
  else:
    print(f'Your final bill is: ${total_price}.')








print("The Love Calculator is calculating your score...")
name1 = input().lower() # What is your name?
name2 = input().lower() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1.lower()
name2.lower()

name1 += name2.lower()
name1.lower()

t = name1.count('t')
r = name1.count('r')
u = name1.count('u')
e = name1.count('e')

first_digit_score = t + r + u + e


l = name1.count('l')
o = name1.count('o')
v = name1.count('v')
e = name1.count('e')

second_digit_score = l + o + v + e
#print(first_digit_score, second_digit_score)
love_score = int(str(first_digit_score) + str(second_digit_score))
#print(love_score)

if love_score < 10 or love_score > 90:
  print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score > 40 and love_score < 50:
  print(f'Your score is {love_score}, you are alright together.')
else:
  print(f'Your score is {love_score}.')
  