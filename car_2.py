# Let's write a class representing a car. 
# This class will contain information about the type of machine, as well as a method for outputting a short description.

class Car():
    # A simple car model.
    def __init__(self, make, model, year):
        # Initializes the attributes of the vehicle description
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        # Returns a neatly formatted description.
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
        
    def read_odometer(self):
        # Displays the mileage of the car in miles.
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        # Sets the setpoint on the odometer
        self.odometer_reading = mileage
        
my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(1787)
my_new_car.read_odometer()