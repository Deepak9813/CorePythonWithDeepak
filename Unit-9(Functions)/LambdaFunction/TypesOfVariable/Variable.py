"""

    Variable:
        #variable is a container that store data.
        #or It is name of memory location that can store data.

        Types of Variable:
        a. global variable:
           # The variable which are declared(defined) outside the function.
           #used(call) anywhere(i.e. inside function, outside function,etc)    

        b. local variable:
                # The variable which are declared(defined) inside the function only.
                # Used(call) inside function only.

        c. non local variable:



"""

# a = 10          #global variable
# print(f"value of a = {a}")

# def show():
#     b = 20          #local variable
#     print("hello")
#     print(f"value of a = {a}")        #access global variable inside function 
#     print(f"value of b = {b}")


# show()



# print(f"Value of b outside the function = {b}")  #local variable is not called(accessed outside the function)


# We can use global variable inside function
# a = 10          #global variable
# print(f"value of a = {a}")

# def show():
#     b = 20          #local variable
#     sum = a+b
#     print(f"Total sum = {sum}")
#     print("hello")
#     print(f"value of a = {a}")        #access global variable inside function 
#     print(f"value of b = {b}")


# show()




#We cannot directly change the value of global variable inside function

#method-2
# a = 10          #global variable
# print(f"Inititally Value of a = {a}")

# def show():
#     global a
#     a = 40          # changing gloabla variable value
#     b = 20          #local variable

#     print(f"value of a after changing value = {a}")


# show()



# print(f"Value of a outside the function after changing = {a}")


#non -local varaible:
# a = 10      #global variable

# def outerFunction():
#     b = 30          #local variable
#     print(f"value of b = {b}")

#     def innerFunction():
#         c = 30      #local variable
#         print(c)
#         print(b+c)          #Here, b is used as global(non local variable) 

#     #Function Call
#     innerFunction()
#     print("hello vai")


# #Function call
# outerFunction()




#========= Try to assign(change) the value of local variable inside innner function ==================

a = 10      #global variable

def outerFunction():
    b = 30          #local variable
    print(f"value of b = {b}")

    def innerFunction():
        nonlocal b
        b = 50  
        
        c = 30      #local variable
        # print(c)
        # print(b+c)          #Here, b is used as global(non local variable) 
        print(f"value of b after change inside inner function = {b}")

    #Function Call
    innerFunction()
    # print("hello vai")
    print(f"value of b after change outside inner function = {b}")





#Function call
outerFunction()