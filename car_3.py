# Let's write a class representing a car. 
# This class will contain information about the type of machine, as well as a method for outputting a short description.

class Car():
    # A simple car model.
    def __init__(self, make, model, year):
        # Initializes the attributes of the vehicle description
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 150
        
    def get_descriptive_name(self):
        # Returns a neatly formatted description.
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
        
    def read_odometer(self):
        # Displays the mileage of the car in miles.
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
    # Sets the setpoint on the odometer. When trying to reverse spin, the change is rejected.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(100)
my_new_car.read_odometer()