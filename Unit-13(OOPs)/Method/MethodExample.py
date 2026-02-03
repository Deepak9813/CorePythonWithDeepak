
#example1
# class Student:
#     college_name = "NCE"        #class atrribute/variable

#     def __init__(self,name,age):
#         self.name = name            #instance attribute(variable)/object varaible
#         self.age = age



#     #instance method/normal methods
#     def show(self):
#         print(f"Student name = {self.name}")
#         print(f"Student age = {self.age}")
#         print(f"Student colleg_name = {self.college_name}")

#     def display(self, father_name, mother_name):
#         # print(f"Student Father Name = {father_name}")
#         # print(f"Student Mother name = {mother_name}")
#         self.father_name = father_name
#         self.mother_name = mother_name

#         print(f"Student Father Name = {self.father_name}")
#         print(f"Student Mother name = {self.mother_name}")




# # create object
# s1 = Student("Deepak", 20)
# # s1.show()    #calling instance method

# s1.display("Ram Bahadur", "Ramita Bhatta")






#example2:

class Student:
    college_name = "NCE"        #class atrribute/variable

    def __init__(self,name,age):
        self.name = name            #instance attribute(variable)/object varaible
        self.age = age



    #instance method/normal methods
    def show(self):
        print(f"Student name = {self.name}")
        print(f"Student age = {self.age}")
        print(f"Student colleg_name = {self.college_name}")

    def display(self, father_name, mother_name):
        # print(f"Student Father Name = {father_name}")
        # print(f"Student Mother name = {mother_name}")
        self.father_name = father_name  
        self.mother_name = mother_name

        print(f"Student Father Name = {self.father_name}")
        print(f"Student Mother name = {self.mother_name}")

    

    def showAll(self):
        print(f"Student father name = {self.father_name}")
        print(f"Student Mother name = {self.mother_name}")





# create object
s1 = Student("Deepak", 20)
# s1.show()    #calling instance method

s1.display("Ram Bahadur", "Ramita Bhatta")
s1.showAll()