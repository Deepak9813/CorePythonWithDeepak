""" 
        Lambda Function:
            # A lambda function is small, anonymous function that does not have name.

            #We use "lambda" keyword to define lambda function.

            #syntax
            lambda parameters:expression


            Here,
            parameters ==> one or more
            but,
            expression ==> only one

            This expression is executed(runs) and return result.


"""

#example1
# result = lambda a,b:a+b

# print(result(2,4))            #function calling




# #example2
# result = lambda a,b:print(a+b)

# result(2,4)  #function calling



# #example3
# result = lambda a,b:print(f"Addition of Two number = {a+b}")

# result(2,4)   #function calling



# #example4:
# result = lambda a,b:print("hello timi kata xau")

# result(2,4)   #function calling



# #example5:
# result = lambda a,b:"Hello kata xau"

# print(result(2,4))   #function calling




""" 
Calculate the average of 3 numbers using lambda function.


"""

result = lambda num1,num2,num3:(num1+num2+num3)/3

# print(result(2,3,5))      #Function call
print(f"Average of 3 numbers = {result(2,3,5)}")









