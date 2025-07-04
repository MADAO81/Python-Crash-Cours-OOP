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