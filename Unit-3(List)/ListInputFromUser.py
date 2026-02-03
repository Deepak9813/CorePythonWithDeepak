"""
Take a list of 3 friends from user.

"""



# #take input from user
# friends = input("Enter your 3 friends seperated by space: ")     #"Drishti Deepak Kiran"

# result = friends.split(" ")      #["Drishti","Deepak","Kiran"]





#take integer number list from user

numList = input("Enter the numbers(elements) of list seperated by space: ")

result = numList.split(" ")      #eg: ["1", "2", "3", "4"]
# print(result)

# map(int,  ["1", "2", "3", "4"])
# final_list = map(int,  result)
final_list = list(map(int,  result))
# final_list = tuple(map(int,  result))
# final_list = set(map(int,  result))

print(final_list)