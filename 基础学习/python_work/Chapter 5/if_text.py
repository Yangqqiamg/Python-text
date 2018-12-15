#one
alien_color = 'green'
if alien_color == 'green':
    print('Player get 5 pont')

alien_color = 'red'
if alien_color == 'green':  #no pass
    print('Player get 5 pont')

#two
alien_color = 'green'
if alien_color == 'green':
    print('Player get 5 pont')
else:
    print('Player get 10 pont')


#three
alien_color = 'red'
if alien_color == 'green':
    print('Player get 5 pont')
elif alien_color == 'yellow':
    print("Player get 10 pont")
else:
    print("Player get 15 pont")


#four
age = 56
if age < 2:
    name = 'baby'
elif 2 <= age <4:
    name = 'bigger baby'
elif 4 <= age <13:
    name = 'child'
elif 13 <= age <20:
    name = 'youth'
elif 20 <= age < 65:
    name = 'adult'
else :
    name = "old"    
print('he is a '+name)

#five
my_food = ['beef','meat','apple','bababas']
if 'akd' in my_food:
    print('you really like akd')
if 'beef' in my_food:
    print('you really like beef')
if 'apple' in my_food:
    print('you really like apple')
if 'akd' in my_food:
    print('you really like akd')
if 'meat' in my_food:
    print('you really like meat')

