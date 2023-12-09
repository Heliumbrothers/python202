







def sum_of_sq(x:int)->int:
    output2 = 0
    final_output = 0
    output = 0
    for integer in range(0, x):
        output = output + integer*integer


    for integer in range(0, x):
        if integer % 2 == 0:
            output2 = output2 + integer*integer
        else:
            output2 = output2 + 0
        
        final_output = output-output2
    

    return final_output

    

    



x = 10



print(sum_of_sq(x))






# bubble sort


# input = [8, 8, 75, 84, 9, 52, 24, 71, 19, ]

# def bubble_sort(input):
#     for x in range(0, len(input)-1):
#         for s in range(0, (len(input))-1):
#             if input[s] > input[(s + 1)]:
#                 temp = input.pop(s)
#                 input.insert(s + 1, temp)

#         print(input)


#     return input

# print("input is " + str(input))
# output = bubble_sort(input)
# print('final result is ' + str(output))