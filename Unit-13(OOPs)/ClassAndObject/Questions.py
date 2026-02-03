"""
Q1. Define a class Car with attributes name and color. Create one object and print its values.
"""


# class Car:
#     #constructor(parameterized constructor)
#     def __init__(self, name, color):
#         self.name = name        #attribute[instance attribute/object attribute]
#         self.color = color



# #create object
# c = Car("BMW", "White")

# # printing the values
# print(c.name)
# print(c.color)



#===================================

class Car:
    #constructor(parameterized constructor)
    def __init__(self, name, color):
        self.name = name        #attribute[instance attribute/object attribute]
        self.color = color
        print("Hello I am parameterized construtor")
        print("K xa fata kukur")
        print(self.name)
        print(name)
        print(color)



#create object
c = Car("BMW", "White")

#printing the values
# print(c.name)
# print(c.color)