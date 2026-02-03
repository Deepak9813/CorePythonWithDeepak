"""
        Dictionary:
        # collection of data where data is stored in key-value pairs,
         where each key is unique and mapped to specific value.

         #It is mutable, ordered, and do not allow duplicate keys.

         #Dictionary is created by curly bracket "{}" and data(key-value pair) is seperated
         by comma. ",".

         syntax:
         dict_var = {
         
                    key1:value1,
                    key2:value2,
                    key3:value2,
                    ------------
         
         }

         Note:
            key must be unique and immutable data type.

"""


# details = {
#         "name":"Kiran",
#         "age":18,
#         "address":"Ktm",
#         1:2000,
#         2:"Ram",
#         30.5:"Pokara",
#         50.2:(1,2,3,4,5),
#         (1,2,3):"Hello",
#         (1,2,4):[1,2,3,4,5,6],
        

# }

# print(type(details))



details = {
    "name":"Deepak",
    "age":26,
    "address":"Mahendranagar,Nepal",
    "weight":68.5,
    "subjects":("English","Math","Science","Biology"),
    "marks":[90,40,50,80,90,100],
    "favPlayers":["Messi","Ronaldo","Neymar"]       

}

# print(type(details))

#============== get(print) entire dictionary ================
# print(details)

# ============= get(print) specifice value from dictionary  ======== dictName[keyname]
# print(details["name"])
# print(details["weight"])

# print(details["subjects"])          #('English', 'Math', 'Science', 'Biology')
# print(details["subjects"][0])          #English

# print(details["marks"])                    #[90,40,50,80,90,100]
# print(details["marks"][3])

# print(details["gender"])                #If key not found then it shows error


# print("jejjejeje")
# print("heleloododkdkdkdkdkekkdkd")



#============== Add data(key-value pairs) in the dictionary ==================
#if key not found in dictionary then add new key-value pair.

# details["gender"] = "Male"

# print(details)


#concept
# details["marks"].append(200000000)        #[90,40,50,80,90,100]
# details["marks"].append("Ram")
# print(details)


#============ update data(key-value pairs) in the dictionary ===========
#if that key already found in dictionary then only update(change) its value.

# details["name"] = "Ram"

# print(details)


#====================== delete data(key-value pair)  ================= synatx: del dictName["keyName"]
# "del" keyword is used for delete data.

# del details["name"]

# print(details)


#concept
# del details["favPlayers"][0]


# print(details)






#================================ Empty Dictionary ====================
# mydict = {} 
# mydict = dict() 

# print(type(mydict))