# Importing the Restaurant class: Take the latest version of the Restaurant class
# and save it in the module. Create a separate file importing the Restaurant class. 
# Create an instance of Restaurant and call one of the Restaurant methods to show
# that the import command is working correctly.

from restaurant import Restaurant

chinese_restaurant = Restaurant("Fried dragon","Chinese cuisine")
italian_restaurant = Restaurant("Tony's cannolis", "Italian bakery")
russian_restaurant = Restaurant("Vladimir's borsch and lard", "Russian cuisine")

chinese_restaurant.describe_restaurant()

italian_restaurant.describe_restaurant()

russian_restaurant.describe_restaurant()