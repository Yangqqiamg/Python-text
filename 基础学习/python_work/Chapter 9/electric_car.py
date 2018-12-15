from car import Car
class Battery():
    def  __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery. ")
        
        pass

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        pass

    def upgrade(self):
        if self.battery_size != 85:
            self.battery_size = 85
        pass


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank(self):
        print("This car doesn's have a gas tank! ")
        pass