"""

    3. Static Method:
        # Does dont use(work with) both instance attribute and class attribute.

        # Defined by @staticmethod decorator.

        # self and cls does not used here.


"""
class Student:
    college_name = "NCE"   #class attribute

    def __init__(self, name, age):
        self.name = name            #instance attribute
        self.age = age 

    
    @staticmethod
    def show():
        # print(f"Student Name = {self.name}")            # error: class method does not use instance attribute and class attribute
        # print(f"Student age = {self.college_name}")                  #error
        # print(f"Student age = {self.college_name}")                  #error
        print("Hello")
        print("hello I am static method and i am fine")
        print("Kata xau")


    @staticmethod
    def add(num1, num2):
        result = num1+num2
        print(result)





#create object
s1 = Student("Deepak", 26)
# s1.show()
s1. add(2,4)


