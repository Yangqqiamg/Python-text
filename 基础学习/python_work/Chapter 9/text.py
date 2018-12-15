#one
class Dog():
	"""docstring for dog"""
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + " is now sitting. ")
		pass

	def roll_over(self):
		print(self.name.title() + " rolled over! ")
		pass

#two
my_dog = Dog('willie', 7)
print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + ' years old. ')


print('')
#three
my_dog.sit()
my_dog.roll_over()


print('')
#four
my_dog = Dog('red', 9)
your_dog = Dog('green', 12)

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + ' years old. ')
my_dog.sit()
my_dog.roll_over()


print("\nyour dog's name is " + your_dog.name.title() + '.')
print("your dog is " + str(your_dog.age) + ' years old. ')
your_dog.sit()
your_dog.roll_over()

print('')
#five
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
        
my_new_car = Car('mike', 'aeg0', 8462)
print(my_new_car.get_descripitve_name())


#six
my_new_car.read_odmeter()

#seven
my_new_car.odmeter_reading = 292
my_new_car.read_odmeter()

#eight
my_new_car.update_odmeter(84)
my_new_car.read_odmeter()

my_new_car.update_odmeter(56)
my_new_car.read_odmeter()

my_new_car.inc_odmeter(15)
my_new_car.read_odmeter()


#nine and "homework 9-9"
'''from car (five)'''
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

my_tesla = ElectricCar('tesla', 'model s', 2006)
print(my_tesla.get_descripitve_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.battery.upgrade()
my_tesla.battery.get_range()

# my_tesla.battery.battery_size = 85
# my_tesla.battery.get_range()


#thirteen
from collections import OrderedDict

flavor_languages = OrderedDict()

flavor_languages['joe'] = 'python'
flavor_languages['mary'] = 'c'
flavor_languages['make'] = 'ruby'
flavor_languages['phil'] = 'python'

for name ,language in flavor_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title())


