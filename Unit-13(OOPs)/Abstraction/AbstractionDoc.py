"""   
        Abstraction:
            # The process of hiding complex implementation details of a class and 
            by showing essential features to the user is known as abstracton.

            # We can achieve abstraction by using:
                1. abstract class
                2. interface.

                

            1. abstract class:
               # Class that contains abstract method(unimplemented method) and may also contain non-abstract method(implemented method) is known as abtract class

                        a. abstract method(unimplemented method):
                            Methods that does not have body is known as abstract method.

                            example:
                            
                            @abstractmethod
                            def show():
                                pass
                                
                            
                            @abstractmethod
                            def display():
                                pass

                        
                            
                        b. non-abstract method(implemented method/normal methos):
                        Methods that  have body is known as non- abstract method.

                        def show():
                            print("Hello I am show method")
                            #body

                
                # Abstract class is a virtual class, it means we cannot create an object of abstract class.

                #Every Abstract class  has at least one child, and that child must implement(override) all the abstract method of abstract class.
                    
                
    
        


"""
from abc import ABC, abstractmethod



class A(ABC):
    
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def show1(self):
        pass



    def display(self):
        print("Hello this is display method")
        print("I am non-abstract method because i have body")
    




# class B(A):

#     #implement abstractmethod of abstract class [method overriding] 
#     def show(self):
#         print("Hello i am show method of class A")
#         print("I am impleted inside class B")

    
#     def show1(self):
#         print("Hello I am show1 method of class A")
#         print("I am implemented inside class B")



#     def hello(self):
#         print("Hello method inside class B")




# b = B()
# b.show()




