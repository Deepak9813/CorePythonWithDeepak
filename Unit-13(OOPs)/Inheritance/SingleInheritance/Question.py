class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    

    def display(self):
        print(f"Brand Name = {self.brand}")

class Bike(Vehicle):
    def __init__(self, name, color, price, brand):
        self.name = name
        self.color = color
        self.price = price
        super().__init__(brand)                  #call constructor   #___init__("Honda")



    #method
    def bike_info(self):
        print(f"Bike Name = {self.name}")
        print(f"Bike Color = {self.color}")
        print(f"Bike Price = {self.color}")
        print(f"Bike Brand = {self.brand}")

 
bike = Bike("Super Splender", "Black", 180000, "Honda")
bike.bike_info()