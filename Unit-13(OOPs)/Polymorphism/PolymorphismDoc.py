"""  
        Polymorphism:
            # Polymorphism is a concept  by which we can perfom a single action in different ways.

            #Polymorphism is derived from two Greek work:- poly means many, morphos means forms, so Polymorphism means having many form.


            # Types of Polymorhism =================
            1. method overloading(compile  time polymorphism): [Python does not support method overloading]
                Method overloading is the concept of haveing more than one method with same name within same class but different parameter list.

            2. method overriding(run time polymorphism):
                Method overding is concept of having method with same name within different class with same parameter list.

"""



# #example of method overloading
# class Deepak:

#     def add(self,a,b):
#         print(a+b)

#     def add(self,a,b,c):
#         print(a+b+c)
    
#     def add(self,a,b,c,d):
#         print(a+b+c+d)


# #create function
# d = Deepak()
# d.add(2,3)
# d.add(3,4,5)
# d.add(1,2,3,4)


#============================== Note: Python Does not support method overloading[But we can perform method overloading by following:] ===============
# class Deepak:    
#     def add(self,a=None,b=None,c=None,d=None):
#         if a is not None and b is not None and c is not None and d is not None:     #if True
#             print(a+b+c+d)
#         elif a is not None and b is not None and c is not None:
#             print(a+b+c)
#         elif a is not None and b is not None:
#             print(a+b)
#         else:
#             print("You entered only one parameter.. You idiot how to add...")
#             print("Please pass at least two values(arguments) to perform operation")



# #create function
# d = Deepak()
# # d.add(1)
# # d.add(2,3)
# # d.add(5,10,15)
# d.add(1,2,4,6)


#============================== method overriding ===============

class Deepak:

    def show(self):
        print("hello I am show method of class Deepak")

    
    def display(self, a):
        print("Display method inside class Deepak")
    
    def info(self, a, b):
        print("Display method inside class Deepak")

class Test(Deepak):
    #method overriding
    def show(self):
        # super().show()          #calling parent class method
        # Deepak.show(self)
        print("hello I am show method overriding inside class Test")
        print("Hello Hello Hello")

    
    def display(self, a):
        print("hello i am display method overriding here in class Test")


t = Test()
# t.show()
# t.display(2)





"""  
Operatior Overloading:
        # When a single operator can perform multiple task is known as operator overloading.

        print(2+3)      #5
        print("Hello" + "World")        #HelloWorld
        print([1,2,3] + [3,5])          #[1,2,3,3,5]


"""
print(2+3)      #5
print("Hello" + "World")        #HelloWorld
print([1,2,3] + [3,5])          #[1,2,3,3,5]
