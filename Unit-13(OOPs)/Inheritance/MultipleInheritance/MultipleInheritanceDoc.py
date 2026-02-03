""" 
    3. Multiple Inheritance:
        In multiple inheritance, a single class is created(derived) from two or more than two or more than two classes.
        syntax:
        class A:
            #properties
            #methods

        class B:
            #properties
            #methods
        
        class C(A, B):
            #properties
            #methods


        
        Here, class A and class B are parent class, class C is sub class.
        Class C is derived(created) from class A and B.
        i.e. Class C inherits the properties and method of its parent class A and B.
        

"""

class A:
    #methods
    def show(self):
        print("I am show method inside class A")
    
    def hello(self):
        print("Hello function inside class A")
    
    def eat(self):
        print("Hello eating inside class A")
    

class B:
    #methods
    def show1(self):
        print("I am show1 method inside class B")
    
    def hello(self):
        print("Hello function inside class B")
    
    def eat(self):
        print("Hello eating inside class B")



class C(A, B):
    #methods
    def show2(self):
        print("I am show2 method inside class C")
        # self.hello()
        super().eat()
    
    def hello(self):
        print("Hello function inside class C")
        # self.hello()
        # A.hello(self)
        # B.hello(self)




#create object
c = C()
# c.show2()
# c.show1()
# c.show()
# c.hello()       #call its own method
# c.eat()          #call class A method because class C inherits class A first
# c.show2()
# c.hello()

