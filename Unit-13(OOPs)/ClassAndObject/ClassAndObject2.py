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

    #method
    def printNameOnly(self):
        print(f"Student Name = {self.name}")
        self.display()




#create object of Student
# s1 = Student("Deepak", 26, "Kathmandu")
# s1.display()            #function(method) call
# s1.printNameOnly()



s2 = Student("Ram", 20, "Butwal")
# s2 = Student(name="Ram", age=20, address="Butwal")
# s2.printNameOnly()
print(s2.name)
print(s2.age)
print(s2.address)