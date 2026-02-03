""" 
    4. Recursive Function(Recursion):
        #When a function call itself again and agian is known as recursive function.


        #syntax:

        #Function Defintion
        def functionName():
            #block of code 
            functionName()          #function that call itself(ie. Recursion)
        
            

        #Function Calling
        functionName()


"""


#example1:

# #function definition
# def show(n):    #n=5
#     print(n)
#     show(n)       #show(5)          #recursion





# #function calling
# show(5)





#example2:

#function definition
def show(n):    #n=5
    print(n)
    if n == 1:
        return
    show(n-1)       #show(5-1)          #recursion
    print("hello Are you fine?")




#function calling
show(5)