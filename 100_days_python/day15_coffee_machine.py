
import sys, os
os.system('cts' if os.name == 'nt' else 'clear')


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
water = 300
milk = 200
coffee = 100
profit = 0

GBP_coin_values = [1, 2, 5, 10, 20, 50, 100, 200]



class CoffeeMachine():
    def __init__(self, water, coffee, milk):
        self.self = self
        self.water = water
        self.coffee = coffee
        self.milk = milk



    def give_coffee(self):
        self.coffee_machine_input = input("what would you like? (espresso/latte/cappuccino)\n")

        if self.coffee_machine_input == "espresso":
            if self.water < 50:
                print("there is not enough water 🙁")
            if self.coffee < 18:
                print("there is not enough coffee 🙁")
            else:
                number_of_50p = int(input("how many 50p coins would you like to give?\n"))
                total_money_given = number_of_50p * 50
                number_of_1pounds = int(input("how many £1 coins would you like to give?\n"))
                total_money_given += number_of_1pounds * 100
                if total_money_given == 150:
                    print(f"money sufficient. enjoy your {self.coffee_machine_input} ☕")
                if total_money_given > 150:
                    print(f"here is your change: £{(total_money_given - 150)/100}")
                    print(f"money sufficient. enjoy your {self.coffee_machine_input} ☕")
                        
                    


        
   
            
        if self.coffee_machine_input == "latte":
            if self.water < 200:
                print("there is not enough water 🙁")
            if self.milk < 150:
                print("there is not enough milk 🙁")
            if self.coffee < 24:
                print("there is not enough coffee 🙁")
            else:
                number_of_50p = int(input("how many 50p coins would you like to give?\n"))
                total_money_given = number_of_50p * 50
                number_of_1pounds = int(input("how many £1 coins would you like to give?\n"))
                total_money_given += number_of_1pounds * 100
                if total_money_given == 150:
                    print(f"money sufficient. enjoy your {self.coffee_machine_input} ☕")
                if total_money_given > 150:
                    print(f"here is your change: £{(total_money_given - 250)/100}")
                    print(f"money sufficient. enjoy your {self.coffee_machine_input} ☕")
                    

        if self.coffee_machine_input == "cappuccino":
            number_of_50p = int(input("how many 50p coins would you like to give?\n"))
            total_money_given = number_of_50p * 50
            number_of_1pounds = int(input("how many £1 coins would you like to give?\n"))
            total_money_given += number_of_1pounds * 100
            if total_money_given == 250:
                print(f"money sufficient. enjoy your {self.coffee_machine_input} ☕")                
            if total_money_given > 250:
                print(f"here is your change: £{(total_money_given - 300)/100}")
                print(f"money sufficient. enjoy your {self.coffee_machine_input} ☕")
                        
            


        

    
        if self.coffee_machine_input == "off":
            if input("password required: ") == "password":
                os.system('cts' if os.name == 'nt' else 'clear')
                sys.exit("this machine was turned off")

        
        

user = CoffeeMachine(300, 200, 100)
while True:
    user.give_coffee()
