name = "Kiran Tamang"
age = 18
weight = 55.5


#output:
# My name is Kiran Tamang , my age is 18 my weight is 55.5 kg.

#normally\
# print("My name is",name,", my age is",age,"my weight is",weight,"kg.")

#string format types:

#1. %string : [old technique]

# print("My name is %s, my age is %i and my weight is %2f kg." %(name,age,weight))




#2. .format: [old technique]
# print("My name is {}, my age is {} and my weight is {} kg.".format(name,age,weight))



#3. f string: [new technique]
print(f"My name is {name}, my age is {age} and my weight is {weight} kg.")



print(f"My name is {name}")
print(f"My age is {age}")
print(f"My weight is {weight} kg.")