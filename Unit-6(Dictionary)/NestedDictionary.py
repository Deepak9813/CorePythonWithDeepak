"""
        Nested Dictionary:
            # A dictionary that contains another dictionary is knwon as nested dictionary.
            

            # A dictionary where value is also a dictionary is known as nested dictionary.
         


"""


details = {
    "roll_no1":{
        "name":"Kiran",
        "age":18,
        "address":"Ktm"
    },
    "roll_no2":{
        "name":"Drishti",
        "age":20,
        "weight":45.60,
        "address":"Dhangadi"
    },
    "gender":"Male",
    "favPlayer":["messi","ronaldo","neymar"]
    
}


# print(details["favPlayer"])            #["messi","ronaldo","neymar"]
# print(details["favPlayer"][0])        #messi


print(details["roll_no1"])          #{'name': 'Kiran', 'age': 18, 'address': 'Ktm'}

print(details["roll_no1"]["name"])  #Kiran

print(details.get("roll_no1").get("name"))  #Kiran

