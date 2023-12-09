


# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
student_total = 0
total_height = 0
for x in range (0, len(student_heights)):
  student_total = student_total+student_heights[x]
print("total height = " + str(student_total))
length_of_Student = len(student_heights)
print("number of students = "+ str(length_of_Student))
average_height = student_total/length_of_Student
average_height = str(round(average_height))
print("average height = "+ average_height)





student_scores = 0
# Write your code below this row 👇
compare_result = 0
compare_1 = 0
compare_2 = 0
for x in range (0, len(student_scores)):
  compare_1 = student_scores[x-1]
  compare_2 = student_scores[x]
  if compare_1 < compare_2:
    compare_result = compare_2
  else:
    compare_result = compare_1
print(compare_result)
  


target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total_even = 0
for x in range(1, (target+1)):
  if x % 2 == 0:
    total_even = total_even + x

print(total_even)




# Write your code here 👇
target = 100
for x in range(1, target + 1):
  if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
  elif x % 3 == 0:
    print("Fizz")
  elif x % 5 == 0:
    print("Buzz")
  else:
    print(x)