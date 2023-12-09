


# #add togerther two digits of a double-digit number

# two_digit_number = input()
# # 🚨 Don't change the code above 👆
# ####################################
# # Write your code below this line 👇
# list(two_digit_number)
# print(int(two_digit_number[0]) + int(two_digit_number[1]))




# #calculates your bmi
# # 1st input: enter height in meters e.g: 1.65
# height = input()
# # 2nd input: enter weight in kilograms e.g: 72
# weight = input()
# # 🚨 Don't change the code above 👆
# height_as_float= float(height)
# weight_as_int = int(weight)
# bmi = weight_as_int / height_as_float**2
# print(int(bmi))
# # Write your code below this line 👇



# # calculates the time we have left to live
# # in weeks, given that we live up to 90 yrs
# # old

# age = input()
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# time_left = 90*52-int(age)*52
# print(f"You have {time_left} left.")



# tip calculator


amount_spent = int(input("how much money did you spend?\n£"))
perc_tip = int(input("what percentage tip would you like to pay? Anywhere between 0 and 15% is OK\n"))
if int(perc_tip) >15 :
    print("that's too high. The max is 15%")
    perc_tip = int(input("what percentage tip would you like to pay? Anywhere between 0 and 15% is OK\n"))
    

money_shared = int(input("how many people would you like to share the cost between?\n"))

money_with_tip = float(amount_spent)*float(perc_tip/100+1)  
money_with_tip = round(money_with_tip,3)
money_with_tip = money_with_tip/money_shared
print("Everyone should pay "+str(money_with_tip))


