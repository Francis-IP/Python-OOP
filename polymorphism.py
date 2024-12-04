# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  # This is a placeholder, to be overridden by subclasses

# Derived class: Car (inherits from Vehicle)
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Derived class: Plane (inherits from Vehicle)
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Create objects
car = Car()
plane = Plane()

# Polymorphism in action
vehicles = [car, plane]
for vehicle in vehicles:
    vehicle.move()  # The move method will behave differently depending on the object
