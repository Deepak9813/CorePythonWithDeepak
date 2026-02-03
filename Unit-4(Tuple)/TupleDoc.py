"""
    Tuple:
        collection of data(elements or data items) which is immutable, ordered, and allow duplicate elements.
        Tuple is generally created by small bracket () and elements of tuple are seperated by comma.
        for example:
        subjects= ("English", "Math", "Science", "Physics")

        We can store different types of data together in a  tuple.
        for example:
        mytuple = (1,"Deepak", 26, "60.55, "Kathmandu")



"""
subjects= ("English", "Math", "Science", "Physics")
mytuple = (1,"Deepak", 26, 60.55, "Kathmandu")

# print(type(subjects))
# print(type(mytuple))


#================= Basic Properties =============
#1. concatenation(+):
# subjects= ("English", "Math", "Science", "Physics")
# mytuple = (1,"Deepak", 26, 60.55, "Kathmandu")

# result = subjects+mytuple
# print(result)


# print(subjects)
# print(mytuple)


#2. indexing: access the specific element from the tuple.
# subjects= ("English", "Math", "Science", "Physics")
# mytuple = (1,"Deepak", 26, 60.55, "Kathmandu")

# # print(subjects[0])
# # print(subjects[1])

# print(mytuple[-1])

#3. slicing:

#4. len():
#5. type():





#=============== Tuple Functions =======================
#only two functions-> count(), index()

# subjects= ("English", "Math", "Science", "Physics", "English", "English")
# mytuple = (1,"Deepak", 26, 60.55, "Kathmandu") 


#count(): count the total number of elements in the tuple

# print(subjects.count("English"))
# print(mytuple.count("Deepak"))
# print(mytuple.count(26))

#index(): give the index number of given element of first occurrence.
# print(subjects.index("English"))   #0
# print(mytuple.index("Deepak"))  #1




#=================== Empty Tuple =========================
# mytuple = ()      #method-1
# mytuple = tuple()             #method-2

# print(type(mytuple))



#questions

# color1 = "Green"
# color2 = "Red"
# color3 = "Yellow"

# favColor = (color1,color2,color3)

# print(favColor)


# ================= About Tuple ================

#1. Is this tuple?  Ans: Yes
# mytuple = 1,2,3,4,5

# print(type(mytuple))      #tuple 

# #2. Is this tuple?  Ans: No
# mytuple = (1)

# print(type(mytuple))        #integer


#3. Is this tuple?  Ans: yes
# mytuple = (1,)

# print(type(mytuple))        #tuple


#4. Is this tuple?  Ans: Yes
# mytuple = 1,

# print(type(mytuple))        #tuple





"""
what is the output of the following code:
a = 2
b = True

print(a+b)


"""

a = 2
b = True   #True means==> 1

print(a+b)
