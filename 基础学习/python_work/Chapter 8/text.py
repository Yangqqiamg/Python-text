#one
def greet_user():
    print('hello')

greet_user()

#two
def greet_user1(name):
    print("hello! " + name)

greet_user1('mike')
    
#three
def describe_pet(pet_name, pet_type = 'pig'):
    print("\nI have a " + pet_type + " named " + pet_name)

describe_pet('dog', 'mary')# wei zhi shi can
describe_pet('cat', 'mike')
describe_pet(pet_type = 'fish', pet_name = "joe")#
describe_pet(pet_name = 'whrite', pet_type = 'fox')
describe_pet('haha')


#four
def get_name(first, last):
	full_name = first + ' ' + last
	return full_name.title()
	pass

new_name = get_name('mary', 'haha')
print(new_name)

#five
def get_full_name(first, last, middle = ''):
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()
	pass

best_name = get_full_name('mart','bidiy')
print(best_name)
good_name = get_full_name('mike', 'joe', 'bob')
print(good_name)


#six
def build_person(first, last, age = ''):
	person = {'first': first, 'last': last}
	if age:
		person['age'] = age
	return person
	pass
message = build_person('matry', 'ddbg', 14)
print(message)

#seven
def get_for_name(first, last):
	full_name = first + ' ' + last
	return full_name.title()
	pass

while True:
	print("\nPlease tell me your name ! ")
	print("(Enter 'quit' at any time to lift)")
	f_name = input("First_name: ")
	if f_name == 'quit':
		break
	l_name = input("Last_name: ")
	if l_name == 'quit':
		break

	full_name = get_for_name(f_name, l_name)
	print("\n Hello " + full_name)

#eight
def greet_users(names):
    for name in names:
        msg = "hello, "+ name.title()
        print(msg)

usersname = ['mike','mary','joe']
greet_users(usersname)

#nine
def print_modles(new_modles,finish_modles):
    while new_modles:
        finish_modle = new_modles.pop()
        print("printint_modle: " + finish_modle)
        finish_modles.append(finish_modle)

def show_modles(finish_modles):
    print("\nThe following modles have been printed: ")
    for finish_modle in finish_modles:
        print(finish_modle)

one = ['ddd','ggg','eee','hhh']
two = []

print_modles(one[:],two)#one[:] is copy from the one
show_modles(two)
print(one)

print(' ')

#ten
def make_pizza(size, *toppings):
    print('\nyou want to add these in your ' +str(size) +  ' - pizza: ')
    for topping in toppings:
        print('-' + topping)

make_pizza(12, 'ddd')
make_pizza(22, 'ddd','ggg','fff')

print(' ')

#eleven
def build_profile(first, last, **user_info):
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
message = build_profile('mike', 'last', num= 12,city= 'shanghai')
print(message)
    

#twelve
import pizza
pizza.make_new_pizza(19, 'pepperoni')


from pizza import make_new_pizza
make_new_pizza(49, 'dgaretr')

from pizza import make_new_pizza as mnp
mnp(97,'asdg', 'adf')

import pizza as p
p.make_new_pizza(75,'daf')

from pizza import *

make_new_pizza(213,'asfa')




        
        
        
        
        	




