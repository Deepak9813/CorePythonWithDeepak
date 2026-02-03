#===================== String Functions ============================

# name = "deEpak raj baij"

#upper(),lower(),casefold():
# print(name.upper())       
# print(name.lower())
# print(name.casefold())          #same as lower()


#capitalize(),title()
# print(name.capitalize())     # Capital first letter only
# print(name.title())           #Capital first letter of every word


#startsWith(), endsWith():   return(gives) True or False
# name = "deEpak raj baij"

# print(name.startswith("d"))    #True
# print(name.startswith("D"))     #False
# print(name.startswith("de"))       #True
# print(name.startswith("deE"))        #True
# print(name.startswith("dx"))          #False

# print(name.endswith("j"))       #True
# print(name.endswith("ij"))      #True
# print(name.endswith("x"))       #False
# print(name.endswith("wij"))     #False


#find(),count():
# name = "deepak raj baij"

# print(name.find("d"))   #0            #find()==>  gives the index number of first occurrence
# print(name.find("e"))   #1
# print(name.find("a"))   #4    
# print(name.find("W"))     #-1           #gives -1, if not found in the string  
# print(name.find("dee"))     #0
# print(name.find("dex"))     #-1

# print(name.count("d"))      #1
# print(name.count("e"))      #2
# print(name.count("dee"))    #1    
# print(name.count("x"))        #0
# print(name.count("dxy"))      #0


#removeprefix(), removesuffix():
# email = "deepak123@gmail.com"
# print(email.removeprefix("deepak123"))
# # print(email.removesuffix("@gmail.com"))

# # website_name = "www.facebook.com"
# website_name = input("please enter your website name: ")
# result = website_name.removeprefix("www.")   #facebook.com
# print(result.removesuffix(".com"))

# msg = "!!!!Hello!!!!!!!!!!!!"
# print(msg.removeprefix("!!!!"))
# print(msg.removesuffix("!!!!!!!!!!!!"))


#strip(),rstrip(),lstrip():
# msg = "!!!!He!llo!!!!!!!!!!!!"
# # print(msg.strip("!"))       #remove all(!) from both side
# # print(msg.rstrip("!"))      #remove all(!) from right side only 
# print(msg.lstrip("!"))      #remove all(!) from left side only   


#split():       break down string and store in list
# name = "Deepak"
# print(name.split("p"))   #['Dee', 'ak']
# print(name.split("a"))     #['Deep','k']
# print(name.split('D'))      #["", "eepak"]
# print(name.split("k"))          #["Deepa", ""]
# print(name.split("e"))            #['D', '', 'pak']

    

#question1: split() function
# name = "DeeDpak"
# print(name.split("D"))   #['', 'ee', 'pak']


# #q2.
# name = "Deeeepak"
# print(name.split("e"))  #['D', '', '', '', 'pak']


#q3.
# name = "Deeeepake"
# print(name.split("e"))  #['D', '', '', '', 'pak', '']


# website = "www.facebook.com"
# result =  website.split(".")        #['www', 'facebook', 'com']
# print(result)
# print(result[1])


#replace():   replace("oldStiring", "newString")
# name = "Deepak"
# print(name.replace("D", "W"))
# print(name.replace("De", "W"))
# print(name.replace("Dee", "xyz"))
