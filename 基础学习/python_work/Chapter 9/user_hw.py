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

