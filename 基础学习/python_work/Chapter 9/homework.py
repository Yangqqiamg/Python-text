#9-1 and 9-2 and 9-4
class Restaurant():
        """docstring for Restaurant"""
        def __init__(self, Restaurant_name,Restaurant_type):
            self.Restaurant_name = Restaurant_name
            self.Restaurant_type = Restaurant_type
            self.num_eat = 0
            self.num_served = 0

        def describe_restaurant(self):
            print("name: " + self.Restaurant_name)
            print("type:" + self.Restaurant_type)

        def open_restaurant(self):
            print("we are opening. ")

        def people_coming(self):
            print("There are " + str(self.num_served) + ' people coming. ')
            pass
	   
        def set_num_served(self):
            message = str(self.num_eat) + " people eating."
            return message
            pass


new = Restaurant('mike','oll day')
new.describe_restaurant()
new.open_restaurant()


#9-3 and 9-5
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempt = 0

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        
    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print("hello! " + full_name + '.')
        
    def inc_login_attempt(self):
        self.login_attempt += 1 
        print(str(self.login_attempt))

    def reset_login_attempt(self):
        self.login_attempt = 0
        print(str(self.login_attempt))


user = User('mike', 'joe')
user.describe_user()
user.greet_user()        

#9-4
restaurant = Restaurant('mike', 'all day')
restaurant.people_coming()

restaurant.num_served = 589
restaurant.people_coming()

restaurant.num_eat = 15
print(restaurant.set_num_served())
        
        
#9-5

new_user = User('mary', 'whrite')
new_user.inc_login_attempt()
new_user.inc_login_attempt()
new_user.reset_login_attempt()
new_user.inc_login_attempt()

#9-6
class IceCreamStand(Restaurant):
    def __init__(self, Restaurant_name,Restaurant_type):
        super().__init__(Restaurant_name,Restaurant_type)
   
    
    def print_ice(self):
        flavor = ['ddd','ggg','hhh']
        print("the ice are follow: ")
        for ice in flavor:
            print('\t' + ice)
            pass    

ice_text = IceCreamStand('mike','allday')
ice_text.print_ice()


#9-7 and 9-8
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


admin_text = Admin("joe","mary")
admin_text.privilege.show_pricileges()

#9-14
from random import randint
class Die():
    def __init__(self,side=6):
        self.side = side

    def roll_die(self):
        for i in range(10):
            x = randint(1,self.side)
            print(str(x))


new_text = Die(20)
new_text.roll_die()











        