"""
            Encapsulation:
            # Wrapping the data(attriubtes) and functions(methods) into a single unit(object) is known as encapuslation.
            for example:
                Class is an example of encapsulation.

            #=================== Main purpose of encaption ===========
             hide data, protect data from access from outside the class.
            [hide data, protect data from outside call]

            
            #In python, we achieve encapsulation using access modifers or property decorator.

            
            #============ Access Modifiers ==================
            # Access modifiers are used to define(set) the visibility or accessibility of class attributes and methods.
            # They determine how the members(attributes & methods) of class can be accessed from outside the class.


"""

#example of encapsulation
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Student Name = {self.name}")
        print(f"Student Age = {self.age}")



#create object
student = Student("Deepak", 26)
student.show()     #calling method
print(student.name)     #calling attributes
print(student.age)