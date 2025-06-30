# Users: Create a class named User. Create two attributes first_name and
# last_name, and then some more attributes that are usually stored in the user's profile. 
# Write the method descripe_user(), which outputs a summary with information about the user. 
# Create another greet_user() method to output a personalized greeting for the user.
# Create multiple instances representing different users. Call both 
# a method for each user.

class User():
    def __init__(self, first_name, last_name,gender,age,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.nationality = nationality
        
    def descripe_user(self):
        print(f"First name - {self.first_name}")
        print(f"Last name - {self.last_name}")
        print(f"Gender - {self.gender}")
        print(f"Age - {self.age}")
        print(f"Nationality - {self.nationality}")
        
    def greet_user(self):
        print(f"Hello dear, {self.first_name} {self.last_name}!" )
        
first_person = User("Hasegawa", "Taizou", "male", 38, "japanese")
first_person.descripe_user()
first_person.greet_user()
print()
second_person = User("Kagura", "Yorozuya", "female", 16, "Yato")
second_person.descripe_user()
second_person.greet_user()