from AbstractionDoc import A

class B(A):

    #implement abstractmethod of abstract class [method overriding] 
    def show(self):
        print("Hello i am show method of class A")
        print("I am impleted inside class B")

    
    def show1(self):
        print("Hello I am show1 method of class A")
        print("I am implemented inside class B")



    def hello(self):
        print("Hello method inside class B")




b = B()
b.show()