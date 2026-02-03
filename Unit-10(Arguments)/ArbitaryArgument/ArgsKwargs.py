"""
        *args and **kwargs:
            #combination of positional arbitary arguments and keyword arbitary arguments.


"""

# #Function Defintion
# def display(*args, **kwargs):
#     print(args)
#     print(type(args))
#     print("=================================")
#     print(kwargs)
#     print(type(kwargs))




# #Function Call
# display(1,2,3,4,5,6,id=1,name="Deepak",age=26,address="Ktm",gender="Male",favPlayer="Messi")






# #example2:
# # #Function Defintion
# def display(*args, **kwargs):
    
#     #get(print) the individual data of args[stored as a tuple]
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(args[3])

#     print("=====================================")
    
#     #get(print) the individual data of kwargs[stored as a dictionary]
#     print(kwargs["id"])
#     print(kwargs["name"])
#     print(kwargs["age"])
#     print(kwargs["gender"])



# #Function Call
# display(1,2,"Deepak",4,5,6,id=1,name="Deepak",age=26,address="Ktm",gender="Male",favPlayer="Messi")







#example2:
# #Function Defintion
def display(*args, **kwargs):
    
    #get(print) the individual data of args[stored as a tuple]  using loop
    for i in args:
        print(i)

    print("=====================================")
    
    #get(print) the individual data of kwargs[stored as a dictionary] using loop
    for i,j in kwargs.items():
        # print(i)
        # print(j)
        print(f"{i} = {j}")



#Function Call
display(1,2,"Deepak",4,5,6,id=1,name="Deepak",age=26,address="Ktm",gender="Male",favPlayer="Messi")