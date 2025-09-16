class Car:
    def __init__(self, make, model, price):
        self.__make = make  # Private variable
        self.__model = model  # Private variable
        self.price = price # public variable
    
    def display(self):
        print(f"Car make: {self.__make}, model: {self.__model}")

car = Car("Toyota", "Corolla", 3000000)
car.display()

# public variable
print(car.price)

# The following will raise an AttributeError
print(car.__make)

# Accessing private variable (not recommended)
print(car._Car__make)  # This works due to name mangling
