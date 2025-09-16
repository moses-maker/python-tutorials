class Car:
    def __init__(self, make, model, total):
        self._make = make  # Protected variable
        self._model = model  # Protected variable
        self.__total = total # private

    def car(self):
        print(self.__total)

# object creation
sports = Car("ferari", "488", 67)
print(sports._make)
sports.car()
print(sports._Car__total) # name mangling.



"""
class SportsCar(Car):
    def __init__(self, make, model, top_speed):
        super().__init__(make, model)
        self.top_speed = top_speed

    def display(self):
        print(f"{self._make} {self._model} with top speed {self.top_speed} km/h")
"""
