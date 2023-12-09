







import sys
import random

print("welcome to the Rock Paper Scissors")
print("type 1 for Rock, 2 for Paper and 3 for Scissors")

player_move = int(input("Choose a number. Do it now!\n"))
if player_move != 1 or 2 or 3:
    print("that's not an option.")
    
else:
    print("thank you. Now, the computer chooses...")

    computer_move = random.randint(1, 3)


    if computer_move == player_move:
        print("it's a draw!")
    else: 
        if computer_move == 1:
            if player_move == 2:
                print(computer_move)
                print("you won!")
            else:
                    print(computer_move)
                    print("you lost!")
        if computer_move == 2:
            if player_move == 1:
                print(computer_move)
                print("you lost!")
            else:
                print(computer_move)
                print("you won!")
        if computer_move == 3:
            if player_move == 2:
                print(computer_move)
                print("you lost!")
            else:
                print(computer_move)
                print("you won!")
        
        
        
