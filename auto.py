#parent class

from abc import ABC, abstractmethod

class Auto:

    def __init__(self, wheels = 4, engine = "Electric", model = "Toyota Prius"):
        """Each player has wheels, a engine, and a model"""
        self.wheels = wheels
        self.engine = engine
        self.model = model

    #set number of wheels
    def setWheels(self, wheels):
        if wheels == 4:
            self.wheels = wheels
            print("You chose a sedan type car")
        elif wheels > 4:
            self.wheels = wheels
            print("You chose a semi truck")

    #set engine type
    def setEngine(self, engine):
        if engine == "Gas":
            self.engine = "Gas"
            print("Your car is gas powered")
        elif engine == "Electric":
            self.engine = "Electric"
            print("Your car is electric powered")
        else:
            print("Please choose Gas or Electric as your engine")

    def setModel(self, model):
        self.model = model
    
    #every car is different and will own version of sell_car
    @abstractmethod
    def sell_car(self):
        pass

    @staticmethod
    def get_class_details():
        print("this is the parent Auto class")

    def start(self):
        print("Engine started... ROOM ROOM")

    def stop(self):
        print("Engine has been turnedd off")