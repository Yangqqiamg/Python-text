#8-1
def display_message():
    print("I learn the hanshu now. ")

display_message()

#8-2
def fa_books(title):
    print("One of my favorite books is " + title)

fa_books('hello tomorrow')

#8-3 and 8-4
def make_shirt(size, num = 'I love python'):
	print("the T-shirt size are " + str(size) + ", num is " + num)

make_shirt('15', 'hah')
make_shirt('84')

#8-5
def describe_city(city, country = 'China'):
	print(city + ' is in ' + country)
	pass
describe_city('shanghai')
describe_city('beijing')
describe_city('newyour', 'usa')

#8-6
def city_country(city, country ):
	message = city + ', ' + country
	return message
	pass
print(city_country('shanghai', 'China'))






 #8-7 and 8-8
def make_album(name, misic_name, num = ''):
        message = {'name': name, 'misic_name': misic_name}
        if num:
            message['num'] = num
        return message
        pass

while True:
            print("\nPlease tell some message ! ")
            print("(Enter 'quit' at any time to lift)")
            f_name = input("name: ")
            if f_name == 'quit':
                break
            l_name = input("misic name: ")
            if l_name == 'quit':
                break
            num = input("misic num(number or no): ")
            if num == 'quit':
                break
            elif num =='no':
                num = ''
            message = make_album(f_name, l_name,num)
        
            print(message)


#8-9
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
    pass

magicians= ['mike','mary','joe']
    
show_magicians(magicians)  

#8-10 and 8-11
def make_great(magicians,greats):
    while magicians:
        great = 'the great ' + magicians.pop()
        greats.append(great)

greats = []
          
make_great(magicians[:],greats)
show_magicians(greats)
show_magicians(magicians)

#8-12
def sanwich(*adds):
    print("\nThese are you add in : ")
    for add in adds:
        print(add)

sanwich('aaa','sss','ddd')
sanwich('qqq','www')
sanwich('zzz')

#8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
message = build_profile('Yang', 'yaya', country= 'China',
                        num= 12,city= 'shanghai')
print(message)
    
#8-14
def car_makes(maker,size,**else_mags):
    massage = {}
    massage['maker'] = maker
    massage['size'] = str(size)
    for key ,value in else_mags.items():
        massage[key] = value
    return massage
    
car = car_makes('mike', 12, color = 'red', big = 'very big')
print(car)
    
#8-15
import models
one = ['ddd','ggg','eee','hhh']
two = []

models.print_modles(one[:],two)#one[:] is copy from the one
models.show_modles(two)
print(one)

print('\n')
#8-16
from models import print_modles
from models import show_modles as sm
one = ['ddd','ggg','eee','hhh']
two = []
print_modles(one[:],two)#one[:] is copy from the one
sm(two)
print(one)

print('\n')

import models as m
one = ['ddd','ggg','eee','hhh']
two = []
m.print_modles(one[:],two)

print('\n')

from models import *
one = ['ddd','ggg','eee','hhh']
two = []

print_modles(one[:],two)#one[:] is copy from the one
show_modles(two)
print(one)



