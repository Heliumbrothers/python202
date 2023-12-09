
def is_odd(x):
    if x%2 != 0:
        return True



my_list = [5,2,6,4,3]

def has_pair_whose_prod_is_odd(input):
    for i in range (0, len(input)-1):
        for x in range (i+1, len(input)):
            print("we are examining the pair of index [{} {}]".format(i, x))
            test = input[i] * input[x] 
            if is_odd(test):
                print("when multiplied together this pair has an odd product")
            

print(" {}".format(has_pair_whose_prod_is_odd(my_list)))