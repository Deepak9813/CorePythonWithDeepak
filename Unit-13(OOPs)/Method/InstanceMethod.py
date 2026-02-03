"""

    1. instance method[normal method/object method/non-static method]:

        # Works with  instance(object) attributes and class attribute.
            
        

        # Defined by self paramter.
        [i.e 1st parameter is self]  

        #instance method called(accessed) using object name only.  



"""


class Student:
    college_name = "NCE"        #class atrribute/variable

    def __init__(self,name,age):
        self.name = name            #instance attribute(variable)/object varaible
        self.age = age


    #instance method/normal methods
    def show(self):
        print(f"Student name = {self.name}")
        print(f"Student age = {self.age}")
        print(f"Student colleg_name = {self.college_name}")




# create object
s1 = Student("Deepak", 20)
s1.show()    #calling instance method
# Student.show()      #error,  instance method cannot be called by using className

