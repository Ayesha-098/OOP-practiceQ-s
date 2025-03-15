# 5. Multiple Inheritance
# Problem: Hybrid Vehicle
# Create a Car class:
# Has speed and method accelerate(amount).
# Create a ElectricVehicle class:
# Has battery_level and method charge_battery().
# Create a HybridCar that:
# Inherits from both Car and ElectricVehicle.

class Car:
    def __init__(self):
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        print(f"Speed: {self.speed} km/h")

class ElectricVehicle:
    def __init__(self):
        self.battery = 100

    def charge_battery(self):
        self.battery = 100
        print("Battery fully charged.")

class HybridCar(Car, ElectricVehicle):
    def __init__(self):
        Car.__init__(self)
        ElectricVehicle.__init__(self)


hybrid = HybridCar()
hybrid.accelerate(50) 
hybrid.charge_battery()