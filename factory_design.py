class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

class AnimalFactory:
    def get_animal(self, animal):
        if animal == "dog":
            return Dog()
        elif animal == "cat":
            return Cat()
        else:
            return None

factory = AnimalFactory()

a1 = factory.get_animal("dog")
print(a1.sound())

a2 = factory.get_animal("cat")
print(a2.sound())
