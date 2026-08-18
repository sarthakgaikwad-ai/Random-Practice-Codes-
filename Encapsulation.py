# Modify the car class to encapsulate the brand attribute,making it private,and provide a getter method for it 
class Car():
    def __init__(self,brand,model):
        self.__brand =brand   #__brand means the attribute has been encapsulated 
        self.model =model

    def get_brand(self):    #This is getter method 
        return self.__brand + "!"

mycar=Car("TATA","Nexon")
print(mycar.get_brand())

# Output 
# TATA!
