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