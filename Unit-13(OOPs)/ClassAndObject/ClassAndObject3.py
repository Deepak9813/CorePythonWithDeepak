#orginally, python gives default constructor if do not create any type of constructor.


#example 1
# class Deepak:
#     #methods
#     def show(self):
#         print("I am show method..")
    
#     def display(self):
#         print("I and display method..")


# #create object of Deepak
# d = Deepak()    #default constructor is used here
# d.show()
# d.display()
    



#technically
class Deepak:
    #constructor(default constructor/no argument constructor)
    def __init__(self):
        # print("Hello i am contructor")
        pass

    #methods
    def show(self):
        print("I am show method..")
    
    def display(self):
        print("I and display method..")


#create object of Deepak
d = Deepak()    #default constructor is used here
d.show()
d.display()