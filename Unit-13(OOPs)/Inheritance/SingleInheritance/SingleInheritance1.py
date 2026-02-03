class Animal:
    #contructor
    def __init__(self, name):
        self.name = name            #attributes(properties)

    def eat(self):
        print("Animal eating")
        print(f"{self.name} eating")


class Dog(Animal):
    #method
    def bark(self):
        print("Dog is barking")
        print(f"{self.name} is barking")



    

#create object
d = Dog("Puppy")
d.bark()
d.eat()
print(d.name)