"""

    Jumping Statment[Access Control Modifiers]: break, continue, pass
        #Jumping statements are used  to control the normal flow of execution of program.

        # Types of Jumping Statement:
        a. break:
            break statement is used to stop(terminate/exit) the loop.

        b. continue:
            #continue statement is used to skip the current iteration(step/round).


        c. pass:
            # does nothing
            # used for future purpose

            we can use pass anywhere in conditional,looping statement,functions,class,etc




"""


#================ example of break statement ============
#example1:
# for i in [1,2,3,30,40]:
#     print(i)
#     break

# print("Hello Deepak")


#example2:
# for i in [1,2,3,30,40]:
#     print(i)
#     break
#     print("Hello kkkdkdk")

# print("Hello Deepak")


#example3:
# for i in [1,2,3,30,40]:
#     print(i)      
#     if i == 3:
#         break

# print("Hello Deepak")


#example4:
# for i in [1,2,3,30,40]:
#     print(i)      
#     if i == 3:
#         break
#     print("kdkdkdkkdk")

# print("Hello Deepak")



#example5:
# for i in range(1,50,1):
#     print(i)      
#     if i == 3:
#         break
#     print("kdkdkdkkdk")

# print("Hello Deepak")




#================ example of continue statement ============
#example1:
# for i in [1,2,3,30,40]:
#     print("Hello Drishti")
#     if i == 3:
#         continue
#     print(i)
#     print("Hello Kiran Vai")

# print("Hello Deepak")


#break
# i = 1

# while i<50:    #while True
#     print(i)
#     print("Hello dipak")
#     if i == 20:
#         break
#     i = i+1
#     #i+=1


#example2:
# i = 1

# while i<5:    #while True
#     print(i)
#     print("Hello dipak")
#     if i == 2:
#         i = i+1
#         continue
#     i = i+1
#     #i+=1


#example2
# i = 1
# while i<5:    #while True
#     print(i)
#     print("Hello dipak")
#     if i == 2:
#         i = i+1
#         continue
#     i = i+1
#     #i+=1
#     print("This is sajha info tech")

#example3:
# for i in range(1,11,1):
#     if i == 5:
#         continue
#     print(i)
#     print("Deepak")

    

#================================ pass statement example ===================
#example:
# if 3>2:
#    pass

#example2:
# email = input("Enter your email: ")
# password = input("Enter your password: ")

# if email=="deepak@gmail.com" and password=="12345":
#     #login kata garne thaxain voli sir lai sodera garxa
#     pass

# else:
#     print("Invalid email or password")

