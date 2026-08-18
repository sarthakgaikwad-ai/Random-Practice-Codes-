# Demonstrate polymorphism by defining a method fuel_type in both Car and Electric Car classes but with different behaviours 
class Car():
    def __init__(self,brand,model):
        self.brand =brand
        self.model =model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type():
        return "Petrol or Diesel"

    
class ElectricCar(Car):      
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type():    #same class diff methods
            return "Electric Charge"


my_tata= Car("TATA","Nexon",)
print(Car.fuel_type())
my_tesla=ElectricCar("Tesala","Zeo5",'90kwh')
print(ElectricCar.fuel_type())
