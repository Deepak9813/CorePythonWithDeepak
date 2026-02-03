"""  
    #Attribute:
        Attribute is a variable that stores data(information)  of an object or a class.

        #============ Class attribute and instance attribute ================

        #Types of Attributes/variable:
        a. Class attribute[class variable]
        b. instance attribute[object attribute/object variable]


        a. class attribute:
            # defined outside the constructor but inside the class.
            # accessed(called) using class name or object name.

            syntax:
            ClassName.attr

            #or
            syntax
            objName.attr
            


            
        b. instance attribute[object attribute]:
            # defined inside the constructor.
            # accessed(called) using object name only.

            syntax:
            objName.attr


"""


class Student:
    #attribute[class attribute]
    college_name = "NCE"

    #constructor
    def __init__(self, name, age):
        self.name = name        #attribute[instance attribute/object attribute]
        self.age = age


    def show(self):
        print(f"Student Name = {self.name}")
        print(f"Student Age = {self.age}")
        print(f"Student College Name = {self.college_name}")
        print(f"Student College Name = {Student.college_name}")


#create object of Student
s1 = Student("Deepak", 26)
# s1.show()


#access(call) instance attribute
print(s1.name)
print(s1.age)
## print(Student.name)       #error, #instance(object) attribute only accessed using object


#acccess(call) class attribute
print(Student.college_name)
print(s1.college_name)


s2 = Student("Ram", 20)
s3 = Student("Deepak", 26)
s3 = Student("Syam", 29)










    
