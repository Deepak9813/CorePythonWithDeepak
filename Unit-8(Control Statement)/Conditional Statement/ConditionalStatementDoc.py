"""

 1. Conditional Statement[Sectional Statement/Desicion making statement]: [if, if-else, if-elif-else]
       # These statements are used to check conditon, and decide(select) which block of code run.

        # Types of Conditional Statement:
            a. if:
                if statement is used to check condtion.
                if the conditon is true, then the code inside if block will run.

                syntax:
                if condition:
                    #body(i.e. body will be executed(run) if the condition is true)


            b. if-else:
                if-else statement is used to check condition.
                # if the condition is true, the code inside if block execute.
                # if the condition is false, the code inside else block execute.

                syntax:
                if condition:
                    #body(i.e. body will be executed if the condition is true)
                else:
                    #body(i.e. body will be executed if the condition is false)


            c. if-elif-else:
                if-elif-else statement is used to check multiple conditions.

                #if statement check first condion.
                #elif statement check next condition.
                #else statement execute when all condtions are false.

                syntax:
                if condition1:
                    #body(i.e. body will be executed when condtion1 is true)
                elif condition2:
                    #body(i.e. body will be executed when condtion1 is false and condition2 is true)
                elif condition3:
                    #body(i.e. body will be executed when condtion1,condition2 are false and conditon3 is true)
                
                .................
                else:
                    #body(i.e. body will be executed when all the condition are false)

    
                

"""


#================================Examples of if statement ==============================
#example:
# a = 2
# b = 3

# if a>b:
#     print("Hello i am inside the if block")
#     print("k xa vai, kata xau")
#     print("a is greater than b")


# print("Hello i am outside the if block")
# print("hey funny boy....")


#example2:
# a = 20
# b = 3

# if a>b:
#     print("Hello i am inside the if block")
#     print("k xa vai, kata xau")
#     print("a is greater than b")
#     exit()


# print("Hello i am outside the if block")
# print("hey funny boy....")



#=========== exit(): exit() is used to terminate(exit) the program ================
# print("hello")
# print("where are you")
# exit()
# print("kdjdjd")
# print("kdkdkdkdkkdd")


#============ nested if or nested if-else: ============
#greatest among three numbers.
# a = 2
# b = 3
# c = 4

# if a>b:
#     if a>c:
#         print("a is greatest")

# if b>a:
#     if b>c:
#         print("b is greater")

# if c>a:
#     if c>b:
#         print("c is greater")



#method-2:
# a = 2
# b = 3
# c = 4

# if a>b and a>c:
#     print("a is greater")

# if b>a and b>c:
#     print("b is greater")

# if c>a and c>b:
#     print("c is greater")





#========================== example of  if-else statement ======================
#program to find greater number
# a = 20
# b = 3

# if a>b:
#     print("Hello i am inside if block")
#     print("a is greater than b")
# else:
#     print("Hello i am inside else block")
#     print("b is greater than a")




#====================== example of if-elif-else =======================
#greatest among 3 numbers
# a = 2
# b = 3
# c = 4
# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))
# c = int(input("Enter value of c: "))

# if a>b and a>c:
#     print("a is greatest")

# elif b>a and b>c:
#     print("b is greatest")

# else:
#     print("c is greatest")




"""
  Q.1  Take gender input from user.
    Print "You are a boy" if user enter Male. otherwise print "You are a girl".
    
"""

# gender = input("Enter your gender(male or female): ").lower()


# if gender == "male":
#     print("You are a boy")

# if gender == "female":
#     print("you are a girl")



"""
Q2. Take email and password from user.
    Print "Login successful" if email is "deepak@gmail.com", and password is "12345"
    otherwise print "Incorrect email or password"


"""





#print even numbers from 0 to 50 using while loop
 
# i = 0

# while i<51:
#     if i%2 == 0:
#         print(i)
#     i = i+1


#or
# i = 0
# while True:
#     if i%2 == 0:
#         print(i)
#     i = i+1

#     if i == 51:
#         break




#1. print even numbers from 0 to 50 using for loop

# for i in range(0,51,1):
#     if i%2 == 0:
#         print(i)


# for i in range(0,51,2):
#     print(i)



# for i in range(1,50,2):
#     print(i)




# for i in [1,2,3]:
#     print(i)
#     break


# print("hello")


for i in [1,2,3,4,5]:
    if i%2==0:
        break