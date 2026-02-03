class A:
    #constructor
    def __init__(self, name):
        self.name = name        #attribute

    #methods
    def showA(self):
        print("Hello I am showA method inside class A")
        print(f"Name = {self.name}")


class B(A):
    #constructor
    def __init__(self, name, age):
        super().__init__(name)      #calling parent class constructor
        # A.__init__(self, name)
        self.age = age

    #method
    def showB(self):
        print("ShowB method inside class B")



class C(B):
    #constructor
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    #method
    def showC(self):
        print("ShowC method is inside class C")
    

    def displayAll(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Address = {self.address}")



#create object of  C
c = C("Deepak", 26, "Kathmandu")
# c.showC()
# c.showB()
# c.showA()
c.displayAll()




