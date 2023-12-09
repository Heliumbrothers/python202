



my_list =[]


other_swap = len(my_list)

n_iteration = int((len(my_list))/2)


temp = 0






for i in range(0, n_iteration):
    print("this is where the swap will happen",other_swap,i)
    temp = my_list[i]
    print(f"{temp} is currently being stored")
    my_list [i] = my_list[other_swap-1]
    print("we are now swapping",other_swap,i)
    my_list[other_swap-1]=temp
    other_swap = other_swap-1
    print()
    print("<next_iteration>")
    



print(n_iteration)







print(my_list)