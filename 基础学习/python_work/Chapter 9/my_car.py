#ten
'''one
from car import Car, ElectricCar

my_new_car1 = Car('audi','a4',2015)
print(my_new_car1.get_descripitve_name())

my_new_car1.odmeter_reading = 59
my_new_car1.read_odmeter()


my_tesla1 = ElectricCar('aaa','ddd',956)
print(my_tesla1.get_descripitve_name())
'''

'''two
#from car import * ( mean add all)
import car

my_beetle = car.Car('qqq','www',279)
print(my_beetle.get_descripitve_name())

my_tesla2 = car.Car('fff','eee',1591)
print(my_tesla2.get_descripitve_name())
'''

from car import Car
from electric_car import ElectricCar

my_new_car1 = Car('audi','a4',2015)
print(my_new_car1.get_descripitve_name())

my_new_car1.odmeter_reading = 59
my_new_car1.read_odmeter()


my_tesla1 = ElectricCar('aaa','ddd',956)
print(my_tesla1.get_descripitve_name())