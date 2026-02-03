"""
Q6. Create a class Shape with method area() that returns 0. Inherit it in Rectangle class and override area() to return length × breadth.

"""


# class Shape:
#     #method
#     def area(self):
#         return 0
    

# class Rectangle(Shape):
#    def __init__(self, length, breadth):
#        self.length = length
#        self.breadth = breadth
       
   
#    #method(method override)
#    def area(self):
#         area = self.length * self.breadth
#         return area
   

# rectangle = Rectangle(2, 3)
# # print(rectangle.area())
# print(rectangle.area(2,3))

 




"""
Q5.
Create a multi-level inheritance where a grandchild class overrides a 
method from the grandparent class. In the overridden method in the grandchild class, 
call grandparent method.”

"""

class GrandParent:
    def show(self):
        print("show method of GrandParent class")

class Parent(GrandParent):
    #override
    def show(self):
        print("show method inside Parent Class.")


class Child(Parent):
    #override
    def show(self):
        print("Hello I am show method of Child class")
        # super().show()
        GrandParent.show(self)

#create object of Child
child = Child()
child.show()



