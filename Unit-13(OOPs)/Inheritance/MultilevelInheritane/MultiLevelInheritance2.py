class A:
    #constructor
    def __init__(self, name):
        self.name = name

    #methods
    def showA(self):
        print("Hello I am showA method inside class A")
        print(f"Name = {self.name}")


class B(A):
    #method
    def showB(self):
        print("ShowB method inside class B")



class C(B):
    #method
    def showC(self):
        print("ShowC method is inside class C")



#create object of  C
c = C("Deepak")
c.showC()
c.showB()
c.showA()




