from auto import Auto
from player import Player
class Gas(Auto):
    def __init__(self,balance = 100000, wheels = 4, engine = "Gas", model = "Nissan Xterra"):
        self.balance = balance
        self.wheels = wheels
        self.engine = engine
        self.model = model

    def set_price(self, price):
        """Set price for any electric car object"""
        self.price = price

    cars = 1


    def sellCar(self, price):
        if self.cars < price:
            print("You have sold the car.")
            self.cars -= 1
        else:
            print("You need a car to sell.")


    def start(self):
        print("Car started... Battery on.")

    def stop(self):
        print("Engine has been turned off.")