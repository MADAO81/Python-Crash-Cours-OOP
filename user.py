class User():
    def __init__(self, first_name, last_name,gender,age,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.nationality = nationality
        
        
    def describe_user(self):
        print(f"First name - {self.first_name}")
        print(f"Last name - {self.last_name}")
        print(f"Gender - {self.gender}")
        print(f"Age - {self.age}")
        print(f"Nationality - {self.nationality}")
        
    def greet_user(self):
        print(f"Hello dear, {self.first_name} {self.last_name}! Nice to meet you!")
       

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

        
class Admin(User):
    def __init__(self, first_name, last_name,gender,age,nationality,privileges):
        super().__init__(first_name, last_name,gender,age,nationality)
        self.privileges = Privileges(privileges)
    
    def admin_rights(self):
        # shows the rights of admin
        self.privileges.show_privileges()