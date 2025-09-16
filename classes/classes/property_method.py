class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @property
    def display(self):
        print(f"My car make is {self.make} and the model is {self.model}")

my_car = Car("Subaru", 875)

# method can be accessed as a variable.
my_car.display