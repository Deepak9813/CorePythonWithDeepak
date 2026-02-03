# name = "Kiran"

#print entire string(data)
# print(name)

#print specific data
# print(name[0])
# print(name[-5])

# =========================== Question =============

# mssg = "Hello This is Deepak From Mahendranager"




# ================ String Properties(String operations) ================
#1. concatenation(+): attach strings
# myVar1 = "Hello"
# myVar2 = "Deepak"

# print(myVar1+myVar2)   #HelloDeepak

# print("Hello"+"Deepak")  #HelloDeepak

# print("K"+"Gardai")      #KGardai

# print("2"+"4")


#2. indexing:  
# accessing the specific element(character) of string.
#syntax:
    #varName[indx_number] or stringName[indx_number]

# name = "Kiran Tamang"

# print(name[0])

# result = name[0]
# print(result)

# print(name[1])  #i    #+ve index
# print(name[-11]) #i   #-ve index
# print(name[5])  #space aauxa
# print(name[-7])



"""
3. Slicing:
        process of accessing the parts(portions) of sequence data type(string,list,tuple,etc.)
        syntax
        varName[start_indx:end_indx:step]   

        Note: 
        # end_indx value is not included.
        # By default, step = 1
        

"""

name = "Deepak"
# address = "Kathmandu"


#=== +ve slicing ==========
# print(name[0:4:1])
# print(name[0:4:])   #By default, step = 1
# print(name[0:4])      #By default, step = 1

# print(name[0:4:1])

# print(name[3:6:1])   #pak
# print(name[3::1])      #pak
# print(name[3::])      #pak

# print(name)             #Deepak
# print(name[0:6:1])
# print(name[0::])        #Deepak
# print(name[::])           #Deepak



#====== -ve slicing ===========
# print(name[-3::1])   #pak
# print(name[-5:-2:1])    #eep


# print(name[3::-1])

# print(name[3:0:-1])

# print(name[-1:-5:-1])





"""
4. length: len()
        Find the length of the string.
        Note: length always start from 1.

"""
# name = "Kiran"
# name1 = "Rejina"
# address = "Bhaktapur"

# print(len(name))

# print(len(name1))

# print(len(address))



# name = "Kiran"

# print("My name is",name)

# # print("Length of name = ",len(name))

# result = len(name)


# print("Length of name =",result)



#4. type():  used to check the data type.(gives the data type)
name = "Deepak"
print(type(name))

#5. id(): gives the memory address
name = "Rejina"
address = "Kathmandu"
print(id(name))
print(id(address))
