"""
    Looping Statement[Iteration statement]:
        # Looping Statement is used to repeats(executes) block of code again again until the conditon becomes false.

        Types of looping:
            a. for: 
                # for loop is used to reapeat block of code for a fixed number of times
                    or loop for through a sequence/iterable(i.e. string, list tuple, range, set, dictionary,etc.)
                
                #syntax:
                for value in iteratable(sequence):
                    #body(i.e. body will be executed until the condition becomes false)


                #or syntax
                for object in iterable:
                    #body(i.e. body will be executed until the condition becomes false)



            
            b. while:
                # While loop is used to repeat(execute) block of code until the conditon becomes false.

                Syntax:
                while condition:
                        #body(i.e block of code will be repeated(executed) util the condition becomes false.)
 
"""



#====================== examples of for loop ==================
#example1:
# for el in [1,20,30,40,100]:
#     print(el)
#     print("I am inside for loop")
#     print("Hello Kata xau")
#     print(2+2)



# print("I am outside the loop")
# print("Hello Hello Hello")


#example2:
# for i in [2,3,4,5,909,100]:
#     print(i)


#example:
# for name in ["Deepak", "Drishti", "Kiran", "Rejina"]:
#     print(name)




#example: ========== string ========
#example1:
# for i in "Deepak":
#     print(i)
#     print("Hello")

#or
# name = "Deepak"
# for i in name:
#     print(i)
#     print("Hello")

#======= set =======
# for el in {1,20,30,40}:
#     print(el)



#============= range() =======================
# for i in range(1,21,1):
#     # print(i)
#     # print("Hello")
#     print("Hello",i)


#============ dictionary ===========

# details = {
#     "name":"Kiran",
#     "age":19,
#     "address":"Ktm",
#     "weight":50.35,
#     "faculty":"Science",
#     "fatherName":"Kkdkdk"
# }

# for i,j in details.items():
#     # print(i)
#     # print(j)
#     print(f"{i} = {j}")


#or ============
# data = ["Deepak", "Drishti", "Kiran", "Rejina"]
# for name in data:
#     print(name)


#for future(in django)
# data = Student.objects.all()   #eg: ["Deepak", "Drishti", "Kiran", "Rejina"]
# for name in data:
#     print(name)





#======================== while loop example =============================
#example:
# while True:          #while True
#     print("Hello Deepak")
#     print("Kata xau")



# while 2>1:          #while True
#     print("Hello Deepak")
#     print("Kata xau")



# i = 1

# while i<5:     # while 1<5
#     print(i)
#     print("hello deepak")
#     i=i+1
#     #i+=1


# i = 1

# while i<51:     # while 1<5
#     print(i)
#     i=i+1
#     #i+=1



#while True:
# i = 1

# while True:
#     print(i)
#     i=i+1
#     if i == 50:
#         break
  


#or
# i = 1

# while True:
#     print(i)

#     if i == 50:
#         break
#     i=i+1


#or
# i = 1
# while True:
#     print(i)
#     i=i+1
#     if i == 51:
#         break



