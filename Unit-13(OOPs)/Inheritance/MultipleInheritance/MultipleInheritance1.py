class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print("Animal eating")
        print(f"{self.name} eating")


class Mammal:
    def __init__(self, breed):      #breed = type 
        self.breed = breed
    

    def running(self):
        print("Mammal running")
        print(f"Mamal breed = {self.breed}")


class Dog(Animal, Mammal):
    def __init__(self, name, breed, age,):
        self.age = age
        Animal.__init__(self, name)   #calling parent class constructor
        Mammal.__init__(self, breed)

    def bark(self):
        print("Dog bark")
        print(f"Dog age = {self.age}")



#create object
d = Dog("Puppy", "Husky", 2)
d.bark()
d.eat()
