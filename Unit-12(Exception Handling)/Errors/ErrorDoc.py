"""  
    Error:
        # Error is a bug(or mistake) in program that occurs during the program compilation or execution
        that distrupts/interrupts the normal flow of code.

        #Types of Errors.
        a. Syntax error:
                The errors that occurs due to the wrong syntax is known as syntax error.

        b. Logical error:
                The errors that occurs due to wrong logic.
                #Note, program runs but wrong output.

        c. Run time error(Exceptions):
                The errors that occours during the execution of program is known as run time error(or exception)
                eg: 
                ValuError, ZeroDivisionError, TypeError, IndexError, keyError,FileNotFoundError,etc. 
        


"""


#syntax error
#example1:
# print("Are you fine")
# print("Kata xau")
# print("Hello Deepak)
      
# print("Last line")



#example
# if 2>1
#     print("Hello I am inside if block")


# print("Hello")



#logical errors
# def add(a,b):
#     print(a*b)          #logical error


# add(2,3)                #output = 6, but it should be 5, it happens because of our wrong logic




#exeptions
# mydict = {
#     "id" :1,
#     "name":"Deepak"
# }

# print(mydict["address"])                #KeyError


#handling
try:
    mydict = {
         "id" :1,
        "name":"Deepak"
        }
    print(mydict["address"])                #KeyError

except KeyError:
    print("Your key is not found in dictionary...")




#example2
# mylist = ["Deepak", 26, "Kanchanpur"]

# print(mylist[6])