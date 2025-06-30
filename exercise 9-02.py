# Restaurant: Create a class named Restaurant. The __init__() method of the Restaurant class
# must contain two attributes: restaurant_name and cuisine_type. Create
# the descripe_ restaurant() method, which outputs two attributes, and the open_restaurant() method, which outputs
# a message that the restaurant is open.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}.")
        print(f"{self.cuisine_type} is served here.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")
        

chinese_restaurant = Restaurant("Fried dragon","Chinese cuisine")
italian_restaurant = Restaurant("Tony's cannolis", "Italian bakery")
russian_restaurant = Restaurant("Vladimir's borsch and lard", "Russian cuisine")

chinese_restaurant.describe_restaurant()
print()
italian_restaurant.describe_restaurant()
print()
russian_restaurant.describe_restaurant()
