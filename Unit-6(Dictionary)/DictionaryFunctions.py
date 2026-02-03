details = {
    "name":"Deepak",
    "age":26,
    "address":"Mahendranagar,Nepal",
    "weight":68.5,
    "subjects":("English","Math","Science","Biology"),
    "marks":[90,40,50,80,90,100],
    "favPlayers":["Messi","Ronaldo","Neymar"]       

}






#1. keys(): Return(gives) all the keys of dictionary.

# print(details.keys())




#2.values(): Return all the values
# print(details.values())




#3. items(): Return all key-value pairs as tuple.
# print(details.items())



#4. get(): Return(gives) value of given key

# print(details.get("name"))
# print(details.get("marks"))         #[90, 40, 50, 80, 90, 100]

# print(details.get("marks")[1])
# print(details["marks"][1])

# print(details.get("gender"))

# print(details.get("gender","key not found in the dictionary"))
# print(details.get("name","key not found in the dictionary"))

# print("==============================")
# print("kdkdkdkkdkdkdd")
# print("dkkdjdn dkdddddddddddddddddddddddddddddddddddddddddddddd")




#5. clear(): clear all the key-value pairs of the dictionary.
# details.clear()
# print(details)


#6. update(): add new key-value pair if that key not exists in dictionary, if exists then only update(its) value.
#yedi tyo key dictionary ma xa vane, tesko value matra change garxa, natra new key-value pair add garxa

# details.update({"gender":"Male","faculty":"IT","name":"Kiran"})

# print(details)


#7. setdefault():       setdefault(key,value)
#yedi tyo key dictionary ma xa vane, tesko value change gardaina(remains as it is), natra new key-value pair add garxa.

# details.setdefault("gender","Male")
# details.setdefault("name","Drishti")

# print(details)



#8. pop(): remove key-value pair of given key
# details.pop("name")
# details.pop("marks")
# print(details)


#9. popItem(): remove last key-value pair of dictionary
# details.popitem()

# print(details)