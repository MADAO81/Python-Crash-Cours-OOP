# Restaurant: Create a class named Restaurant. The __init__() method of the Restaurant class
# must contain two attributes: restaurant_name and cuisine_type. Create
# the descripe_ restaurant() method, which outputs two attributes, and the open_restaurant() method, which outputs
# a message that the restaurant is open.
# Users:  Add an attribute 
# number_served with a default value of 0; it represents the number of served
# visitors. Create an instance named restaurant. Print the number_served value,
# then change it and print it again.
# Add a method named set_number_served(), which allows you to set the number of served users. 
# Call the method with the new number and print the value again.
# Add a method named increment_number_served(), which increases the number of served users by a specified amount.
# Call this method with any number that could represent the number of customers served, for example, in one day.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}.")
        print(f"{self.cuisine_type} is served here.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")
        
    def show_number_served(self):
        # shows the number of customers served
        print(f"The restaurant served {self.number_served} customers.")
        
    def set_number_served(self, customers_served):
        # sets the number of clients served
        self.number_served = customers_served
        
    def increment_number_served(self, increment):
        # Increases the quantity of served customers
        self.number_served += increment
        
        

restaurant = Restaurant("Joe's burgers","American cuisine")
print(f"{restaurant.restaurant_name}.")
print(f"{restaurant.cuisine_type}.")
print()
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()
restaurant.set_number_served(20)
restaurant.show_number_served()
print()
restaurant.increment_number_served(15)
restaurant.show_number_served()