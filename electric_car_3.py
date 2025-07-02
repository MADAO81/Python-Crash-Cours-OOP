# Let's try to build an electric car model. An electric car is a specialized type of car, so a new
# class of ElectricCar can be created based on the Car class written earlier.
# Then we will have to add to it the code of attributes and behavior related only
# to electric vehicles.

class Car():
    """Simple car model."""
    
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
        
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
class Battery():
    """Simple battery model for electric car """
    
    def __init__(self, battery_size=75):
        """ Initializes the attributes of the accumulator."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Displays information about battery power """
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """Outputs the approximate power reserve for the battery. """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")
        
class ElectricCar(Car):
    """Represents aspects of the machine specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initializes the attributes of the parent class.
        Then initializes attributes specific to the electric vehicle.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def describe_battery(self):
        """Displays information about the battery capacity."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
my_tesla = ElectricCar("tesla", "model s", "2019")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()