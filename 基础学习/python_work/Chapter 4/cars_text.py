#one 
cars=['dazong','fengtian','bengtian','bieke']
for car in cars:
    if car =='bengtian':
        print(car.upper())
    else:
        print(car.title())

#two
car='jakey'
print(car=='jakey')   #will show Ture
print(car=='not')   #will show False

#three
car = 'NUM'
print (car == 'num')    #will show False
print (car.lower() == 'num')    #will show ture

#four
car = 'love'
if car != 'bieke':
    print('I do not want this car')
else:
    print('I will buy it')


#five
age = 50
if age != 50:
    print('you are worng ! Please try again')
else:
    print("you win !")


#six
age = 100
if age < 80 and age > 20:
    print("you are ture")
else:
    print("you lose")    

if age >15 or age < 20:
    print ("you ture")

#seven
cars=['dazong','fengtian','bengtian','bieke']
if 'dazong' in cars:    #Ture
    print ('ture')
if 'andrew' not in cars:    #Ture
    print ('you are right')





