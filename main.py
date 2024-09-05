class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def drive(self, speed):
        print("Driving the", self.year, self.model, "at", speed, "kmph.")

class BMW(Vehicle):
    def drive(self, speed):
        Vehicle.drive(self, speed)  

class Ferrari(Vehicle):
    def drive(self, speed):
        Vehicle.drive(self, speed)  

def drive_car(car):
    car.drive(210)

bmw = BMW("M5", 2022)
ferrari = Ferrari("F8", 2021)

drive_car(bmw)
drive_car(ferrari)
