


import sys

print("welcome to TREASURE ISLAND...")
print("...you have been sent to find treasure.")
print("you come to a cross-road. do you go left or right?")
print("type LEFT or RIGHT")
crossroads = str(input())
if crossroads == "LEFT":
    print("you get to a river. do you swim across or wait for a boat?")
    river = str(input("type WAIT or SWIM\n"))
    if river == "SWIM":
        print("GAME OVER. YOU DIED")
        SystemExit
    else:
        print("you get to a hall with 3 doors. they are red, blue and yellow.")
        print("which door do you open?")
        door = str(input("type RED, BLUE or YELLOW\n"))
        if door == "RED":
            print("GAME OVER. YOU DIED")
            SystemExit
        if door == "BLUE":
            print("GAME OVER. YOU DIED")
            SystemExit
        if door == "YELLOW":
            print("the door opens up to the treasure vault.")
            print("WELL DONE!")
            SystemExit
else:
    print("GAME OVER. YOU DIED")
    SystemExit