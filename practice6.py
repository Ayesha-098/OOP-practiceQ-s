# 4. Single Inheritance
# Problem: Smart Home Device
# Create a Device class:
# Stores device_name and status (ON/OFF).
# Implements toggle_status() to switch ON/OFF.
# Create a subclass SmartBulb:
# Inherits Device and adds brightness (0-100).
# Implements adjust_brightness(level).

class Device:
    def __init__(self, device_name, status):
        self.device_name = device_name
        self.status = status
    
    def toggle_status(self):
        if self.status == "OFF":
            self.status = "ON"
        else:
            self.status = "OFF"
            print(f"{self.device_name} is now {self.status}")
    
class SmartBulb(Device):
    def __init__(self, device_name, status = "OFF", brightness=0):
        super().__init__(device_name, status)
        self.brightness = brightness


my_bulb = SmartBulb("Living Room Bulb")
my_bulb.toggle_status()

print(f"{my_bulb.device_name} is {my_bulb.status}")



        
