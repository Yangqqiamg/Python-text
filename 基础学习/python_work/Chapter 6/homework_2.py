#6-5
rivers = {
    'big river': 6,
    'medium river': 4,
    'small river': 1,
    }
for name,num in rivers.items():
    print(name.title() + ' through ' + str(num) + ' cities')
print()
for name in rivers.keys():
    print(name)
print()
for num in rivers.values():
    print(str(num))
print()


#6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
members = ['mike','jen','mary','edward']
for member in favorite_languages.keys():
    if member in members:
        print('thank you ! ' + member.title())
    else:
        print('hello! ' + member.title() + ' do you want '+
            'to join in us ?')
            
    
    
    
    
    
    
    
    
