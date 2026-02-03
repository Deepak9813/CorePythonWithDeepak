class A:
    #methods
    def showA(self):
        print("Hello I am showA method inside class A")


class B(A):
    #method
    def showB(self):
        print("ShowB method inside class B")



class C(B):
    #method
    def showC(self):
        print("ShowC method is inside class C")



#create object of  C
c = C()
c.showC()
c.showB()
c.showA()




