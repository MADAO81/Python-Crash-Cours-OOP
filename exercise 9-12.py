from user_1 import User 
from admin import Privileges, Admin 

class Admin(User):
    def __init__(self, first_name, last_name,gender,age,nationality,privileges):
        super().__init__(first_name, last_name,gender,age,nationality)
        self.privileges = Privileges(privileges)
    
    def admin_rights(self):
        # shows the rights of admin
        self.privileges.show_privileges()