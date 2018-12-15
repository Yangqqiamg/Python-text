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

        