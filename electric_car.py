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
        
class ElectricCar(Car):
    """Represents aspects of the machine specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """initializes the attributes of the parent class."""
        super().__init__(make, model, year)
        
my_tesla = ElectricCar("tesla", "model s", "2019")
print(my_tesla.get_descriptive_name())