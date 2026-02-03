#========== Properties =====================
# marks= [90,30,40,70,80,90,30]
# fruits = ["apple", "mango", "orange", "banana", "mango"]

#1. +(concatenation): attach into single list
# print("Hello"+"Deep")       #HelloDeep
# print([1,2,3]+[80,90,40])     #[1, 2, 3, 80, 90, 40]

# mylist1 = [1,2,3]
# mylist2 = [80,90,40]

# print(mylist1+mylist2)          #[1, 2, 3, 80, 90, 40]


#2. indexing: process of access the individual(specific) element from the list.
# marks= [900,30,40,70,80,90,30]
# fruits = ["apple", "mango", "orange", "banana", "mango"]

# print(marks[0])         #900
# print(marks[-7])

# print(fruits[2])        #orange



"""
        3. slicing:  
        process of accessing the parts(portion) of list.
        synatx:
        varName[start_indx:end_index:step]  or listName[start_indx:end_index:step]

        Note:
        end_indx ==> value not included
        step = 1, by default

"""



marks= [900,30,40,70,80,90,30]
# fruits = ["apple", "mango", "orange", "banana", "mango"]


# print(marks[0:3:1])     #[900, 30, 40]

# print(marks[1:6:1])     #[30, 40, 70, 80]

# print(fruits)
# print(fruits[0:5:1])        #['apple', 'mango', 'orange', 'banana', 'mango']
# print(fruits[0::1])        #['apple', 'mango', 'orange', 'banana', 'mango']
# print(fruits[::1])        #['apple', 'mango', 'orange', 'banana', 'mango']

# print(fruits[0:4:1])           #["apple", "mango", "orange", "banana"]
# print(fruits[-5:-1:1])          #['apple', 'mango', 'orange', 'banana']


# print(fruits[::-1])               #['mango', 'banana', 'orange', 'mango', 'apple']

fruits = ["apple", "grapes", "orange", "banana", "mango"]

print(fruits[4:0:-1])              #['mango', 'banana', 'orange', 'grapes']

print(fruits[2::-1])                   #[orange', 'grapes',"apple"]