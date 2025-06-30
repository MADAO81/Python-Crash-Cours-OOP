# Each instance created based on the Dog class will contain a nickname. 
# (name) and age; in addition, it will contain the sit()
# and roll_over() methods.

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