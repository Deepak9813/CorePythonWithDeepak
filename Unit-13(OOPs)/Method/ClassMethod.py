"""  
        Class Method:
            # Works with class attribute(varible) only.

            # Defined by using @classmethod and cls.
                i.e. # Defined by using @classmethod decorator
                     # 1st parameter is cls.

            # class method called(accessed) by using both object name & class name.
            

            


"""

class Student:
    college_name = "NCE"        #class attribute(variable)

    def __init__(self,name,age):
        self.name = name        #instance attribute
        self.age = age
    
    @classmethod
    def show(cls):
        # print(f"Student name = {cls.name}")     #error, classmethod does not accept(use) instance attribute
        # print(f"Student age = {cls.age}")         #error, classmethod does not accept(use) instance attribute
        print(f"Student college name = {cls.college_name}")
        

#create an object
s1 = Student("Deeak", 26)
# s1.show()     #calling classmethod using objectName
Student.show()  #calling clasmethod using ClassName



