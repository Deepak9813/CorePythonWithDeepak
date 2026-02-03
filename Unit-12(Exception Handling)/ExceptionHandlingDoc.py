"""  
    # =============== Exception =====================
    Exception is an unwanted/unexcepted events that occurs during the execution the program 
        that distrupts(interrupts) the normal flow of program.


    
    #============= Why exception occurs? ==================
    1. invalid user input,
    2. file not found,
    3. network error,
    4. arithemetic error(eg:cannot divide by zero)


    #=========== Exception Handling ===============
    Exception handling is the process of managing(handling) the exceptions.

    #or 
    Exception handling is the process of managing(handling) the unwanted/unexcepted events that occurs during the execution the program 
        that distrupts(interrupts) the normal flow of program.

    
    In python, we can handle exceptions using try-except block.
    Where,
    try ==> try block always contains the risky code[i.e. the code that may raise(throw) an exception]

    except ==> except block catches and handle an exception if it occurs.


    syntax:
    try:
        #risky code
        #Here,we write the code that may raise(throw) an exception

    except SomeExceptionType:
        #code to hanlde the exception  if it occurs
    


"""

#xample of exception occur:
# print(5/0)

# print("Hello Deepak")
# print("Are you fine?")


#exception handling
# try:
#     print(5/2)
#     # print("kata xau")

# except ZeroDivisionError:
#     print("You cannot divide by zero")



# print("Hello Deepak")
# print("Are you fine?")


#or[If we do not know the type of exception]
# exception handling
try:
    print(5/0)
    # print("kata xau")

except Exception as e:
    # print("Error aayo hai")
    print(f"your error = {e}")
    # print(e)



print("Hello Deepak")
print("Are you fine?")


