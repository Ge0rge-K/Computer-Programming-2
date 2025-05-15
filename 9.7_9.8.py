# Base class
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")

# Privileges class
class Privileges:
    def __init__(self, privileges=True):
        if privileges is True:
            privileges = ["can timout post", "can delete post", "can ban user", "can make others admin"]
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Admin class using Privileges
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

# Test
admin_user = Admin("George", "Koniaris")
admin_user.describe_user()
admin_user.privileges.show_privileges()
