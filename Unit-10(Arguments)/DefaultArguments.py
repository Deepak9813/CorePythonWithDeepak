"""  
    Default Arguments:
        # parameter that also have default value.
        # if value(argument) is passed than that argument is stored in parameter, otherwise use default value.

        #default values are always written in last.

"""


#example:
def display(name,age,address, college= "NCIT", mssg = "Hello How are you"):
    print(f"Student Name = {name}")
    print(f"Student Age = {age}")
    print(f"Student Address = {address}")
    print(f"Student College = {college}")
    print(f"Student Message = {mssg}")



# display("Deepak", 26, "Kanchanpur")
# display("Deepak", 26, "Kanchanpur","NCE")
# display("Deepak", 26, "Kanchanpur","NCE", "This is Deepak From Sajha Info Tech")



display(name="Deepak", age=26, address="Kanchanpur", college="NCE")
