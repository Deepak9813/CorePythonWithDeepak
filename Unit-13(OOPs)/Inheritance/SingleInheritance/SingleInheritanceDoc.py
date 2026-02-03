"""
        # 1. Single Inheritance:
                #In single inheritance, there is only one parent class and only one child class.
                
                syntax:
                class A:
                    #properties
                    #methods
                
                class B(A):
                    #properties
                    #methods


                
                In the above syntax, class A is parent class, class B is chlid class.
                Class B inherits(recieves) the properties and methods of parent class A.

"""

""" 
    self:
        # self is  reference parameter that refers to the current object.
        # it is used to access(call) properties and methods within the same class.

"""


class A:
    #methods
    def show(self):
        print("hello  I am show method inside class A")
    
    def show1(self):
        print("hello i am show1 method inside class A")
        # self.show()     #own function call 



class B(A):
    def display(self):
        print("I am display method inside class B")

    def display1(self):
        print("I am display method inside class B")
        # self.display()     #own function call 
        super().show()       #calling parent class method



#create object of B
b = B()
b.display()
b.display1()
b.show()
b.show1()




    


