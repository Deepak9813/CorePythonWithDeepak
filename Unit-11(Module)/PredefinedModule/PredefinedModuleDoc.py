"""  
        Predefined Module(inbuilt module):
            # The module which is already defined  by python is known as predefined module.



"""

# #example[using import statement]
# import math


# # print(math.pow(2,3))
# # print(math.sqrt(16))
# # print(math.ceil(3.33333999999999))   #just above integer value
# # print(math.ceil(4.22222222222))


# # print(math.floor(3.33333999999999))     #just below integer value
# # print(math.floor(4.22222222222))



#example[using from statement]
# from math import pow,sqrt,ceil,floor
# from math import *



# print(pow(2,3))
# print(sqrt(16))
# print(ceil(3.33333999999999))   #just above integer value
# print(ceil(4.22222222222))


# print(floor(3.33333999999999))     #just below integer value
# print(floor(4.22222222222))





#===================== random module ====================

import random

computer = random.choice(["win", "loss", "draw"])
print(f"computer data={computer}")

user = input("Please enter any one of this [Win or Loss or Draw]: ").lower()
# user.lower()
print(f"user data = {user}")


if user == computer:
    print("Match Draw")

elif user == "win" and computer == "loss":
    print("You Won")
elif user == "win" and computer == "draw":
    print("You Won")

else:
    print("You loss")
    print("Computer win")



