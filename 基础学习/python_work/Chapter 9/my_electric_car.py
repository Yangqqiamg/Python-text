#twelve
from car import ElectricCar

my_tesla1 = ElectricCar('aaa','ddd',956)
print(my_tesla1.get_descripitve_name())
my_tesla1.battery.describe_battery()
my_tesla1.battery.get_range()