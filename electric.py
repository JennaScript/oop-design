from auto import Auto
class Electric(Auto):

    def __init__(self, cars = 1, price = 50000, wheels = 4, engine = "Electric", model = "Tesla"):
        self.price = price
        self.cars = cars
        self.wheels = 4
        self.engine = engine
        self.model = model


    def set_price(self, price):
        """Set price for any electric car object"""
        self.price = price



    def sellCar(self, price):
        if self.cars < price:
            print("you have sold the car")
            self.cars -= 1
        else:
            print("you need a car to sell")


    def start(self):
        print("Car started...Battery on")

    def stop(self):
        print("Engine has been turnedd off")


new_car = Electric(1, 50000, 4, model= "Tesla")
new_car.setEngine("Electric")
new_car.set_price(100000)
print(new_car.price)