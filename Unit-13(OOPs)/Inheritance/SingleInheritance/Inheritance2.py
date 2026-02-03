class Animal:
    #contructor
    def __init__(self, name, age):
        self.name = name            #attributes(properties)
        self.age = age

    def eat(self):
        print("Animal eating")
        print(f"{self.name} eating")
        print(self.age)


class Dog(Animal):
    #constructor
    def __init__(self, color,name, age):
        self.color = color          #attribute
        # super().__init__(name, age)                     #__init__("Puppy", 2)
        Animal.__init__(self, name, age)                     #__init__("Puppy", 2)
        
      
    #method
    def bark(self):
        print("Dog is barking")
        print(f"{self.name} is barking")



d = Dog("Black", "Puppy", 2)
d.eat()


#create object

