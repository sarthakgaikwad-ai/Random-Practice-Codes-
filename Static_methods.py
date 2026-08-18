# Add a static method to the car class that returns a general description of a car 

class Car():
    def __init__(self,brand,model):
        self.brand =brand
        self.model =model
        
    @staticmethod
    def general_des():
        return "Cars are amazing mode of transport"


print(Car.general_des())
