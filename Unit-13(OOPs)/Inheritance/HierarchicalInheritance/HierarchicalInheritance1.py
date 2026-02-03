
class A:

    def __init__(self, a):
        self.a = a
    #method
    def show(self):
        print(f"value of a = {self.a}")
        print("Hello I am show method inside class A")



class B(A):
    def __init__(self, a, b):
        # super().__init__(a)   #calling constructor
        A.__init__(self, a)
        self.b = b

    #method
    def show1(self):
        print(f"value of a = {self.a}")
        print(f"value of b = {self.b}")
        print("I am show1 method inside class B")


class C(A):
    def __init__(self, a, c):
        # super().__init__(a)
        A.__init__(self, a)
        self.c = c

    #method
    def show2(self):
        print(f"value of a = {self.a}")
        print(f"value of c = {self.c}")
        print("I am show2 method inside class ")


#create object
c = C(10, 20)
# c.show2()       #calling own class method
# c.show()        #calling parent class method


b = B(2,3)
b.show1()
b.show()