#=================== Set functions ======================

# mySet = {1,2,3,4}

#1. add():   add single element into the set
# mySet.add(100)
# mySet.add("Ram")

# print(mySet)


#2. update(): add set into set
# mySet.update({30,45,"Deepak","ktm"})
# print(mySet)

# set2 = {30,45,"Deepak","ktm"}
# mySet.update(set2)
# print(mySet)

# #3. clear(): clear all elements of the set
# mySet = {1,2,3,4}

# mySet.clear()
# print(mySet)



#4. remove():  remove the given element from the set.
# mySet = {1,2,3,4,"Deepak"}

# # mySet.remove(2)
# # mySet.remove("Deepak")
# mySet.remove("Drishti")     #error, if element not found in the set

# print(mySet)


#5. discard(): same as remove() fuction but it does not show error when element not found.
# mySet = {1,2,3,4,"Deepak"}


# # mySet.discard(2) 
# # mySet.discard("Deepak") 
# # mySet.remove("Drishti") 
# mySet.discard("Drishti")

# print(mySet)


# print("Hello this is Deepak")
# print("k xa brother")
# print("I am from Mahendranagar")



#6.pop(): remove the random element from the set.

# mySet = {1,2,3,4,"Deepak", 1.5, 0.5, False}
# mySet.pop()

# print(mySet)



#7.union(): Gives the set that contains the elements of both set.
# set1 = {1,2,3,4,"Deepak"}
# set2 = {1,2,3,50,"Drishti", "Kathmandu"}

# print(set1.union(set2))


# 8. intersection(): gives the set that contains the element that belongs to both set.
# set1 = {1,2,3,4,"Deepak"}
# set2 = {1,2,3,50,"Drishti", "Kathmandu"}

# print(set1.intersection(set2))


# 9. difference(): 
# set1 = {1,2,3,4,"Deepak"}
# set2 = {1,2,3,50,"Drishti", "Kathmandu"}

# # print(set1.difference(set2))        #Gives the set that contains that contains elements in set1 but not in set2

# print(set2.difference(set1))



#10.symmetric_difference(): Gives the set combining elements of both set except common element.[]

# set1 = {1,2,3,4,"Deepak"}
# set2 = {1,2,3,50,"Drishti", "Kathmandu"}


# print(set1.symmetric_difference(set2))      #(set1_union_set2)-(set1_intersection_set2)


#11. intersection_update():     
set1 = {1,2,3,4,"Deepak"}
set2 = {1,2,3,50,"Drishti", "Kathmandu"}

print(set1)
print(set2)

# set1.intersection_update(set2)      #first intersection nikalxa, ani agaadiko set ma intersection set rakhxa
set2.intersection_update(set1)      #first intersection nikalxa, ani agaadiko set ma intersection set rakhxa


print(set1)
print(set2)
