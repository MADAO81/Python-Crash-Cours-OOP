# Battery upgrade: Use the final version of the program  electric_car.py 
# Add a method named upde_battery() to the Battery class. This
# method should check the battery size and set the power to 100 if
# it has a different value. Create an instance of an electric vehicle with a battery after the call, 
# call get_range(), and then call get_range() a second time after the call 
# upgrade_battery(). Make sure that the power reserve has increased.


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
        
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
        
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
print("Let's upgrade battery of this vehicle!")
print("Now:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()