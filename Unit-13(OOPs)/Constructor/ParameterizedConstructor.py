class Student:
    #constructor(special method/function)
    def __init__(self, name, age, address):
        self.name = name        #attributes/properties/variables
        self.age = age 
        self.address = address


    #method(function)
    def display(self):
        print(f"Student Name = {self.name}")
        print(f"Student Age = {self.age}")
        print(f"Student Address = {self.address}")

    


#create object of Student
s1 = Student("Deepak", 26, "Kathmandu")
s1.display()            #function(method) call
