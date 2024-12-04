# Base class: ElectronicDevice
class ElectronicDevice:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    def charge_battery(self):
        self.battery_percentage = 100
        print(f"{self.model} is fully charged!")

# Derived class: Smartphone (inherits from ElectronicDevice)
class Smartphone(ElectronicDevice):
    def __init__(self, brand, model, battery_percentage, camera_quality):
        super().__init__(brand, model, battery_percentage)
        self.camera_quality = camera_quality

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def take_picture(self):
        print(f"Taking a picture with {self.camera_quality} quality.")

# Create a smartphone object
my_phone = Smartphone("Apple", "iPhone 14", 50, "12MP")
my_phone.charge_battery()  # Method from ElectronicDevice class
my_phone.make_call("123-456-7890")  # Method specific to Smartphone class
my_phone.take_picture()  # Method specific to Smartphone class
