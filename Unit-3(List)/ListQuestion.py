"""

1. Write a program to add your 3 favourite players in a list using append() function.

"""

#method -1
# myList = []    #empty list
# # myList = list()                 #list()==> constructor[special function]

# myList.append("Rejina")
# myList.append("Sita")
# myList.append("Kiran")

# print(myList)



#method-2
# myList = []    #empty list

# favPlayer1 = "Rejina"
# favPlayer2 = "Sita"
# favPlayer3 = "Kiran"

# myList.append(favPlayer1)
# myList.append(favPlayer2)
# myList.append(favPlayer3)

# print(myList)



"""

2. Write a program to add your 3 favourite players in a list using append() function.
Note: Take 3 favourite players as input from user.

"""

myList = []    #empty list

favPlayer1 = input("Enter your 1st fav player name: ")
favPlayer2 = input("Enter your 2nd fav player name: ")
favPlayer3 = input("Enter your 3rd fav player name: ")

myList.append(favPlayer1)
myList.append(favPlayer2)
myList.append(favPlayer3)

print(myList)
