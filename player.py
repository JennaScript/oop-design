import random
from auto import Auto
from electric import Electric
from gas import Gas

class Player():
    """Start the player off with a set amount of money"""
    def __init__(self, balance):
        # super().__init__(50000)
        self.balance = 50000

    cars = 0

    def spin_cash_wheel(self, cash):
        """add money by rolling virtual dice"""
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        print(f"{num1}, {num2}")
        self.balance += (num1 * num2)
    
    def buyCar(self, price):
        """Buy car"""
        if self.balance > price:
            self.balance -= price
            self.cars += 1 
            print("You've bought this car") 
        else:
            print("Sorry. You don't have enough money to buy this car!")


    def sell_car(self, price):
        """Sell car"""
        if self.cars > 1:
            self.balance += price
            self.cars -= 1
        else:
            "You're unable to sell a car due to havingg no cars."