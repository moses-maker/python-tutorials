class Vehicle:
    def __init__(self, model):
        self.model = model

    def vehicle_model(self):
        print(f"Vehicle Model name is {self.model}")

class Bike(Vehicle):
    def vehicle_model(self):
        print(f"Vehicle Model name is {self.model}")

class Car(Vehicle):
    def vehicle_model(self):
        print(f"Vehicle Model name is {self.model}")

class Aeroplane(Vehicle):
     def vehicle_model(self):
        print(f"Vehicle Model name is {self.model}")


# Function, that recieving
def vehicle_info(vehicle_obj):
    vehicle_obj.vehicle_model()

ducati = Bike("Ducati-Scrambler")
beetle = Car("Volkswagon-Beetle")
boeing = Aeroplane("Jets")

#vehicle_info(ducati)

for each_object in [ducati, beetle, boeing]:
    """
    each_object = ducati
    vehicle_info(each_object)

    each_object = beetle
    vehicle_info(each_object)

    each_object = boeing
    vehicle_info(each_object)
    """
    vehicle_info(each_object)
