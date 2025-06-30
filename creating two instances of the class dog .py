# Creating two instances of the class Dog
class Dog():
    """A simple dog model"""
    def __init__(self, name, age):
        """Initializes the name and age attributes."""
        self.name = name 
        self.age = age 
    
    def sit(self):
        """The dog sits down on command"""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """The dog rolls over on command"""
        print(f"{self.name} rolled over!")
        
my_dog = Dog("Willie-G",6)
your_dog = Dog("Dyna",3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
