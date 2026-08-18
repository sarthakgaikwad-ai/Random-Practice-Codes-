#Create an Electric car class that inherits from car class and has an additional attribute battery size 
class Car():
    def __init__(self,brand,model):
        self.brand =brand
        self.model =model

    def full_name(self):
        return f"{self.brand} {self.model}"

    
class ElectricCar(Car):      #New child class created 
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

my_tata= ElectricCar("TATA","Nexon","89kwh")
print(my_tata.full_name())
print(my_tata.battery_size)
        
