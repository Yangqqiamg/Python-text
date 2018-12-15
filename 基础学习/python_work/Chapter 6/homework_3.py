#6-7
people_1 = {
    'first_name': 'add',
    'last_name': 'mike',
    'age': 24,
    'city': 'shanghai',
    }

people_2 = {
    'first_name': 'bobe',
    'last_name': 'joe',
    'age': 23,
    'city': 'beijing',
    }

people_3 = {
    'first_name': 'add',
    'last_name': 'whtle',
    'age': 44,
    'city': 'shandong',
    }

peoples = [people_1,people_2,people_3]

for x in peoples:
	print(x)

print('\n')

#6-8
baby = {
	'leixing': 'dog',
	'master': 'mike',
	}
honey = {
	'leixing': 'cat',
	'master': 'mary',
	}
tomy = {
	'leixing': 'fish',
	'master': 'white',
	}

pets = [baby,honey,tomy]
for pat in pets:
	print(pat)

print('\n')

#6-9
favorite_plase = {
	'mike': ['beijing','shanghai'],
	'mary': ['shandong'],
	'joe': ['hangzhou','sichuan','xizhang'],
	}
for name, places in favorite_plase.items():
	print('\n' + name.title() + "'s favorite plase :")
	for plase in places:
		print('\t' + plase)

print('\n')

#6-11
cities = {
	'shanghai': {
		'country': 'China',
		'population': 100000,
		'fact': 'now',
		},

	'beijing': {
		'country': 'China',
		'population': 1456400,
		'fact': 'low',
		},

	'shandong': {
		'country': 'China',
		'population': 155500,
		'fact': 'big',
		}
	}
for city, massage in cities.items():
	print('\ncity: '+ city.title())
	country = massage['country'].title()

	print('\tcountry: ' + country )
	print('\tpopulation: ' + str(massage['population']))
	print('\tfact: ' + massage['fact'])










