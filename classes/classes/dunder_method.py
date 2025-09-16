class Car:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return f"Car type is {self.description}"


# object creation
my = Car("bugatti")

print(my)