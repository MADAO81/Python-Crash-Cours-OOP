# Users: Create a class named User. Create two attributes first_name and
# last_name, and then some more attributes that are usually stored in the user's profile. 
# Write the method descripe_user(), which outputs a summary with information about the user. 
# Create another greet_user() method to output a personalized greeting for the user.
# Create multiple instances representing different users. Call both 
# a method for each user.
# Write the increment_login_attempts() method, which increases the value of login_attempts
# by 1. Write another method named reset_login_attempts(), which resets the value of login_attempts.
# Create an instance of the User class and call increment_login_attempts() several times. 
# Print the login_attempts value to make sure that the value has been changed correctly, and then call reset_login_attempts(). Print login_attempts again
# and make sure that the value is set to zero.


class User():
    def __init__(self, first_name, last_name,gender,age,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.nationality = nationality
        self.login_attempts = 0
        
    def descripe_user(self):
        print(f"First name - {self.first_name}")
        print(f"Last name - {self.last_name}")
        print(f"Gender - {self.gender}")
        print(f"Age - {self.age}")
        print(f"Nationality - {self.nationality}")
        
    def greet_user(self):
        print(f"Hello dear, {self.first_name} {self.last_name}!" )
        
    def show_login_attempts(self):
        # Displays the login attempts
        print(f"{self.login_attempts} login attempts  were made")
        
    def increment_login_attempts(self):
        # Increases the login attempts 
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        # Resets the login attempts
        self.login_attempts = 0
        
        
person = User("Hasegawa", "Taizou", "male", 38, "japanese")
person.descripe_user()
person.greet_user()
print()
person.show_login_attempts()
person.increment_login_attempts()
person.show_login_attempts()
person.increment_login_attempts()
person.increment_login_attempts()
person.increment_login_attempts()
person.show_login_attempts()
person.reset_login_attempts()
person.show_login_attempts()

