class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odmeter_reading = 0

    def get_descripitve_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
        
    def read_odmeter(self):
        print("This car has " + str(self.odmeter_reading) + " miles on it. ")


    def update_odmeter(self, mileage):
        if mileage >=self.odmeter_reading:
            self.odmeter_reading = mileage
        else:
            print("you can't do it !")
    
    def inc_odmeter(self, miles):
        self.odmeter_reading += miles

    def fill_gas_tank(self):
        print("This full !")
        pass

