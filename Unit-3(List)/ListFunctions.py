#============ List Functions ==================
# numList = [30,40,70, 90, 50, 30, 40]

#1.append(): add single element in the list
# numList.append("Ram")
# numList.append(9000)

# print(numList)

#2. extend():  add list into the list
# numList.extend(["apple", "orange", "mango"])
# numList.extend([20,"Ram","Hello", 30.5])

# print(numList)


#sort():   sort in accending order
# numList = [30,40,70, 90, 50, 30, 40]

# numList.sort()  
# # numList.sort(reverse=False)  

# print(numList)



#sort(reverse = True): sort the list in descending order
# numList = [30,40,70, 90, 50, 30, 40]

# numList.sort(reverse=True)
# print(numList)



#reverse(): reverser the list
# numList = [30,40,70, 90, 50, 30, 40]

# numList.reverse()

# print(numList)



#clear(): clear the list[i.e. remove all element from the list]
# numList = [30,40,70, 90, 50, 30, 40]

# numList.clear()

# print(numList)



#remove(): remove the first occurrence element from the list
# numList = [30,40,70, 90, 50, 30, 40]

# # numList.remove(30)
# # numList.remove(40)

# print(numList)


#pop(): remove element at given index  [pop(index)]
# numList = [30,40,70, 90, 50, 30, 40]

# # numList.pop(0)          #remove element at 0 index
# numList.pop(1)            


# print(numList)


#insert(): add(insert) element at given index.[insert(index,element)]
# numList = [30,40,70, 90, 50, 30, 40]

# # numList.insert(0, "Ram")        #add "Ram" at 0 index
# numList.insert(2,900000)

# print(numList)



#copy():
# numList = [30,40,70, 90, 50, 30, 40]

# result = numList.copy()

# print(numList)
# print(result)


#sorted(): sort the list in accending order but does not change in orginal list
# numList = [30,40,70, 90, 50, 30, 40]

# result = sorted(numList)

# print(numList)
# print(result)


#count(): count the total number of elements. [count(element)]
# numList = [30,40,70, 90, 50, 30, 40]

# print(numList.count(30))
# print(numList.count(70))


