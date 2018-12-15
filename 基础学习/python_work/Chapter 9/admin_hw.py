from user_hw import User

class Privileges():
    def __init__(self,):
        self.privileges = ["can add post","can delete post","can ban user"]
    
    def show_pricileges(self):
        print("What admin can do: ")
        for privilege in self.privileges:
            print("\t" + privilege)
        pass


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name,last_name)
        self.privilege = Privileges()