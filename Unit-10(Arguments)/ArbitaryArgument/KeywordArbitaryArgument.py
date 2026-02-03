"""
        Keyword Arbitary Argument(**kargs): prefix(**)
            #Used we do not know how many number keyword arguments(values) are passed into the function.

            #collected(stored) as a dictionary.



"""


# #example1:
# #function definiton
# def display(**a):   #a = sab argument aauxa in the form of dictionary
#     print(a)
#     print(type(a))



# #function call
# display(id=1,name="Deepak",age="26",address="Ktm",subject="Python",gender="Male",weight=70.5, ispaid=True)








# #example2:
# #function definiton
# def display(**a):   #a = sab argument aauxa in the form of dictionary
#     # print(a)
#     # print(type(a))

#     #get(print) individual data
#     print(a["id"])         #dictName["keyName"] or dictName.get("keyName")
#     print(a["name"])
#     print(a["age"])
#     print(a["gender"])
#     print(a["weight"])    #simailary others



# #function call
# display(id=1,name="Deepak",age="26",address="Ktm",subject="Python",gender="Male",weight=70.5, ispaid=True)







#example3:
#function definiton
def display(**a):   #a = sab argument aauxa in the form of dictionary
    # print(a)
    # print(type(a))

    #get(print) individual data using loop
    for i,j in a.items():
        # print(i)
        # print(j)
        # print(i,j)
        print(f"{i} = {j}")
    

#function call
display(id=1,name="Deepak",age="26",address="Ktm",subject="Python",gender="Male",weight=70.5, ispaid=True)