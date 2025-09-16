class Car:
    # class variable
    wheel = 4

    def __init__(self, make, model):
        self.make = model
        self.model = model

    @staticmethod
    def update_wheels(number):
        wheels = number
        print(f"The car has {wheels} wheels.")

    @staticmethod
    def display():
        print("Hello i am static")

# create an object based on the class
my_car = Car("4 wheel", "Subaru")

# how to access class methods
my_car.update_wheels(7)
Car.update_wheels(7) # access class method using the class name

# allow access to a method as a variable
my_car.display