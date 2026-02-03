"""
        Positional Arbitary Argument(*args): prefix(*)
            #Used we do not know how many number positional arguments(values) are passed into the function.
            #collected(stored) as a tuple.

"""

# #example1:
# #Function definiton
# def display(*a):     #a = ("Deepak", 1, "Ktm", "Male", "deepak@gmail.com", "Python With Django")
#     print(a)
#     print(type(a))



# #functon call
# display("Deepak", 1, "Ktm", "Male", "deepak@gmail.com", "Python With Django")








# #example2:
# #Function definiton
# def display(*a):     #a = ("Deepak", 1, "Ktm", "Male", "deepak@gmail.com", "Python With Django")
#     # print(a)
#     # print(type(a))
#     for i in a:
#         print(i)


# #functon call
# display("Deepak", 1, "Ktm", "Male", "deepak@gmail.com", "Python With Django")







# #example2:
# #Function definiton
# def display(*a):     #a = ("Deepak", 1, "Ktm", "Male", "deepak@gmail.com", "Python With Django")
#     # print(a)
#     # print(type(a))
#     for i in a:
#         print(i)
#         if i == "Male":
#             break

# #functon call
# display("Deepak", 1, "Ktm", "Male", "deepak@gmail.com", "Python With Django")






#example4:
#Function definiton
def display(h,*a):     #h = "Deepak",a = (1, "Ktm", "Male", "deepak@gmail.com", "Python With Django")
    
    print(h)
    print(type(h))
    
    print(a)
    print(type(a))
    


#functon call
display("Deepak", 1, "Ktm", "Male", "deepak@gmail.com", "Python With Django")




