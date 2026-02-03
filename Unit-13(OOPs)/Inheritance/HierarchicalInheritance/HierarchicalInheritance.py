"""
        4. Hierarchical Inheritance:
            # In Hierarchical inheritance, two or more than two child are created(derived) from a single super class.
            i.e. there is only one parent class and two or more than two child class.

            syntax:
            class A:
                #properties
                #methods
            
            class B(A):
                #properties
                #methods
            
            class C(A):
                #properties
                #methods

            
            In the above syntax, Class A is parent class, class B and C are child class. Class B and C inherits
            the attributes and method of parent class A.   
            
            
            

"""


class A:
    #method
    def show(self):
        print("Hello I am show method inside class A")



class B(A):
    #method
    def show1(self):
        print("I am show1 method inside class B")


class C(A):
    #method
    def show2(self):
        print("I am show2 method inside class ")


#create object
c = C()
c.show2()       #calling own class method
c.show()        #calling parent class method

b = B()
b.show1()       #calling own class method
b.show()        #calling parent class method