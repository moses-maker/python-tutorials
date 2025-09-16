class Car:
    # class variable
    wheel = 4
    def __init__(self, make, model):
        self.make = model
        self.model = model

    @classmethod
    def update_wheels(cls, number):
        cls.wheels = number

    @classmethod
    def display_wheels(cls):
        print(f"The car has {cls.wheels} wheels")
    
    def display(self):
        print(self.make, self.model)

# create an object based on the class
my_car = Car("4 wheel", "Subaru")

# accessing instance method
my_car.display()

# how to access class methods
my_car.update_wheels(7)
my_car.display_wheels() # access class method using the object
Car.display_wheels() # access class method using the class name
