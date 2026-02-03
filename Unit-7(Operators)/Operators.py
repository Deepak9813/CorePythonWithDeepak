"""
        Operators:
            # Operators is a symbol that performs certain operations between operands.
            for example:
            c = a + b

            #Here,
            =,+  are operators.
            a,b,c are operands.

            #Types of Operatiors:
            1. Arithmetic Operators: 
                    a. + (addition operator)
                    b. - (subtraction operator)
                    c. * (multiplication operator)
                    d. / (division operatior)
                    e. % (modulus operator)
                    f. ** (power operator or exponential operatior)
                    g. // (floor division operatior)

                    
            2. comparasion operator(Relational operatior):
                    #Used to compare two values.
                    #Return True or False.
                a. == (equal to operator)
                b. != (not equal to )
                c. >  (greater than)
                d. >= (greater than or equal to)
                e. < (less than)
                f. <= (less than or equal to)

                

        3. Assignment Operator:
                a. = (assignment operatior)
                b. +=(addition assignment operator)
                c. -=
                d. *=
                e. /=
                f. %=
                g. **=
                h. //=


        4. Logical Operatior:
                a. or
                b. and 
                c. not


        5. Membership Operator:
                #membership operator is used to check value exists(present) in the sequence(eg:string,list,tuple,etc.) or not.
                #Returns True if value exist(present) otherwise return False.
                a. in
                b. not in
        
                
        6. Identity Operator:
                #Checks the memory location of two objects(variable).
                #Return True or False.

                a. is:
                        #Returns True if both object(variable) have same memory location, otherwise return False.

                b. is not:
                        #Return True if both object(variable) have not same memory location, otherwise return False.

                        

        7. Bitwise operator:            works on bit.
                a. | (Bitwise or operator)
                b. & (Bitwise and operator)
                c. ~ (Bitwise not operator)    #Shitt + TapKoMathikoButton
"""

#1. Arithmetic Operator: [+, -, *, /, %, **, //]
# a = 5
# b = 2

# print(a+b)        #7
# print(5+2)

# print(a-b)          #3
# print(a*b)          #10
# print(a/b)          #2.5
# print(a%b)            #1                   #gives remainder
# print(11%3)         #2

# print(a**b)           #25
# print(2**5)             #32

# print(a//b)             #2




#2. Comparison Operator(Relational Operator):  [==, !=, >, >=, <, <=]
#Return True or False

# a = 5
# b = 2

# print(a == b)  #False
# print(a != b)    #True
# print(a>b)      #True
# print(a>=b)     #True
# print(a<b)          #False
# print(a<=b)         #False


#3. Assignment opertors: [=, +=, -=, *=, /=, %=, **=, //=]
# a = 5
# b = 2

# a+=b            #a = a+b
# a-=b             #a = a-b
# a+=5            #a = a+5 
# a*=b            #a = a*b
# a/=b            #a = a/b
# a**=b           # a = a**b   
# a%=b               # a = a%b   

# a//=b             #a = a//b              

# print(a)






#4. Logical operatiors: or, and, not
        #Works on boolean values.[i.e. Return True or False]


# print(True or True)             #True

# print(5>2 or 3<1)                # print(True or False)            #True

# print(True or False)            #True
# print(False or False)           #False
# print(False or True)               #True

# print(True and True)            #True
# print(True and False)           #False


# print(5>2 and 3<1)              #print(True and False)  #False




#5. Membership Operators:  

# print("d" in "deepak")        #True
# print("dp" in "deepak")         #False
# print("wx" in "deepak")         #False


# print("d" not in "deepak")        #False
# print("dp" not in "deepak")        #True
# print("wx" not in "deepak")         #True


# name = "deepak"

# print("d" in name)              #True



#6. Identity Operators: is, is not

# a =[1,2,3]
# b= [10,20,30]

# c = [1,2,3]

# d = a

# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))


# print(a == c)         #True             #== operator checks value
# print(a is c)           #False

# print(a is d)         #True

# print(b is c)           #False
# print(c is d)           #False


# print(a is not c)       #True
# print(c is not d)       #True

# print(a is not d)       #False




# x = 10
# y = 20
# z = 10

# print(id(x))
# print(id(y))
# print(id(z))


# print(x == z)   #True           #value check
# print(x is z)   #True           #memory location check




#7. Bitwise Operators: |, & , ~

a = 5
b = 2

# print(a|b)              #7
# print(a&b)              #0

# print(~a)               #~5         #add 1 and add -ve sign          #-6


print(~(a|b))           #~7                     #add 1 and add -ve sign #-8

    

