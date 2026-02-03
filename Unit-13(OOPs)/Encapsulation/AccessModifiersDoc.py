"""  
     #============ Access Modifiers ==================
            # Access modifiers are used to define(set) the visibility or accessibility of class attributes and methods.
            # They determine how the members(attributes & methods) of class can be accessed from outside the class.

            #==================== Types of Access Modifers ================
            1. public:  
                #members(attributes and methods) can be accessed from anywhere(inside class and outside the class)
                #example:
                name = "Deepak"
                show()

                Note: these are public attribute and method


            2. private: [prefiexed by double underscore(_ _)]
                #members(attributs and methods) can be accessed only inside that class but not outside the class.
                example:
                __name = "Deepak"
                __show()

            3. protected:  [prefiexed by single underscore(_)]
                #members(attributes and methods) can be accessed only inside that class and its child class but not outside these classes.
                example:
                _name = "Deepak"
                _show()
             
                
            Note: python members(attributes and methods) are not 100% private.
            From outside the class, We can access members(attributes and methods) of class using Name mangling.
            i..e:
            objName._ClassName__attributeName
            objName._ClassName__methodName()

"""


# #=================== example using public access modifers =============================
# class Student:
#     #constructor
#     def __init__(self, name, age):
#         self.name = name            #public instance attribute
#         self.age = age

#     def show(self):             #public instance method
#         print(f"Student Name = {self.name}")
#         print(f"Student Age = {self.age}")



# #create object
# student = Student("Deepak", 26)
# student.show()     #calling method [okay==> because it is public function]
# print(student.name)     #calling attributes  [okay==> because it is public attribute]
# print(student.age)


# #=================== example using private access modifers =============================
# class Student:
#     #constructor
#     def __init__(self, name, age):
#         self.__name = name            #private instance attribute
#         self.__age = age

#     def __show(self):             #private instance method
#         print(f"Student Name = {self.__name}")
#         print(f"Student Age = {self.__age}")
    
#     def display(self):          #public instance method
#         print("I am display method")
#         self.__show()


#create object
# student = Student("Deepak", 26)
# student.display()   #called because it is public method
# student.__show()     #calling method [not callable ==> because it is private function]
# print(student.__name)     #calling attributes  [not callable ==> because it is private attribute]
# print(student.__age)
# student.display()  #called because it is public method

# #using name manglining, we can access these attributes and methods of class [But never use this in coding]
# student._Student__show()
# print(student._Student__name)
# print(student._Student__age)





#=================== example using protected access modifers =============================
#example1
# class Student:
#     #constructor
#     def __init__(self, name, age):
#         self._name = name            #protected instance attribute
#         self._age = age

#     def _show(self):             #protected instance method
#         print(f"Student Name = {self._name}")
#         print(f"Student Age = {self._age}")
    
#     def display(self):          #protected instance method
#         print("I am display method")
#         self._show()



# #create object
# student = Student("Deepak", 26)
# student._show()         #callable but we do not call according to python rule  # Allowed, but discouraged
# print(student._name)    #Callable but we do not call according to python rule      
# student.display()     



#example2:
class Student:
    #constructor
    def __init__(self, name, age):
        self._name = name            #protected instance attribute
        self._age = age

    def _show(self):             #protected instance method
        print(f"Student Name = {self._name}")
        print(f"Student Age = {self._age}")
    
    def display(self):          #protected instance method
        print("I am display method")
        self._show()


class Test(Student):
    def hello(self):
        print(f"Student Name in Test class = {self._name}")
        print(f"Student age in Test class = {self._age}")
        self._show()




test = Test("Deepak", 26)
test.hello()
