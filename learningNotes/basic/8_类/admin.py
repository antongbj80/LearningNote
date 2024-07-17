from user_1 import User

class Privileges:
    def __init__(self,privileges=[]) :
        self.privileges = privileges

    def show_privileges(self):
        """显示当前管理员的权限"""
        if self.privileges:
            for privilege in self.privileges:
                print(f"-{privilege}")
        else:
            print("- This user has no privileges.")


class Admin(User):
    def __init__(self,first_name,last_name,username, email, location):
        super().__init__(first_name,last_name,username, email, location)
        self.privileges = Privileges()