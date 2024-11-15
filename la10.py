class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    
    def describeVehicle(self):
        print(f"{self.brand} has {self.model} with {self.fuel_type}")

class Motorcycle(Vehicle):
    pass
motorcycle = Motorcycle("Kawasaki", "ZR1000R", "Gasoline")
motorcycle.describeVehicle()

class Car(Vehicle):
    pass
car = Car("Mitsubishi", "Raptor", "Diesel")
car.describeVehicle()