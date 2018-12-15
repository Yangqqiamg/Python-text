##alien
alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])

print('you just earmed ' + str(alien['points']) + ' points')

alien['x_position'] = 5     #add new message
alien['y_position'] = 45    #
print(alien)

del alien['color']
print(alien)
print('\n')




##alien_0
alien_0 = {}    #new empty list
alien_0['color'] = 'red'
alien_0['points'] = 10
print(alien_0)

alien_0['color'] = 'yellow'    #change the 'color'
print(alien_0)
print('\n')




##alien_1
alien_1 = {'x_position': 10,'y_position': 2,'speed': 'slow'}
print("Original x_position : " + str(alien_1['x_position']) )
alien_1['speed'] = 'fast'   #change the speed to change the x_position

if alien_1['speed'] == 'slow':
    x_ex = 1
elif alien_1['speed'] == 'medium':
    x_ex = 3
elif alien_1['speed'] == 'fast':
    x_ex = 5
alien_1['x_position'] = alien_1['x_position'] + x_ex    #add the x_ex
print("New x_position : " + str(alien_1['x_position']))
print('\n')




##favorite_language
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(name + 'favorite language is ' +
        language.title() + '.')
print()

for name in favorite_languages.keys():
# ~ or for name in favorite_languages:
    print(name)        
print()

friends = ['jen','edward']
for name in favorite_languages.keys():
    if name in friends:
        print(name.title() + 'is my best friend !')
    else:
        print(name.title())
        
if 'erin' not in favorite_languages:
    print('please take our poll ! ')
print()

for name in sorted(favorite_languages.keys()):
    print(name)
print()

for language in sorted(favorite_languages.values()):
    print(language)
print()
for language in set(favorite_languages.values()):
    print(language)



##user
user_0 = {
    'username': 'efermi',
    'fist': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print('\nkey : ' + key)
    print('value : ' + value)
print('\n')









