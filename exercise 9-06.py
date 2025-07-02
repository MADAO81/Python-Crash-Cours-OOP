# Ice cream kiosk: An ice cream kiosk is a special kind of restaurant. 
# Write the IceCreamStand class inheriting from the Restaurant class.
# Add an attribute named flavors to store a list of frost varieties. 
# Write a method that outputs this list. Create an instance of Ice Cream Stand
# and call this method.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        description = f"Restaurant name is {self.restaurant_name}. \n{self.cuisine_type} is served here: "
        return description
        
class IceCreamStand(Restaurant):
    
    def __init__(self,restaurant_name, cuisine_type,flavours):
        #initializes the attributes of the parent class
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours
    
    def ice_cream_menu(self):
        # shows the list of ice cream
        for flavour in self.flavours:
            print(flavour)
        
flavours =  ["Vanilla", "Chocolate","Strawberry","Cherry","Lemon", "Mango"]
ice_cream_kiosk = IceCreamStand("The jolly Eskimo","Ice Cream",flavours)
print(ice_cream_kiosk.describe_restaurant())
ice_cream_kiosk.ice_cream_menu()
