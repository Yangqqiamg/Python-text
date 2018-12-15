#one
people=['joke', 'xiaoming', 'joe', 'whinte', 'mary']
print('the first people in the list are :')
for person in people[:3]:
    print(person)


print('\nthe middle people in the list are :')
for person in people[1:4]:
    print(person)
    
print('\nthe last people in the list are :')
for person in people[-3:]:
    print(person)
    
#two
pizas=['panpan','shanhe','bishengke']
friend_pizas=pizas[:]
pizas.insert(1,'jiuyang')
friend_pizas.append('paike')
print(pizas)
print(friend_pizas)

print('\nMy favorite pizza are :')
for piza in pizas:
    print('\t\t'+piza)

print("\nMy friend's favorite pizza are :")
for pizza in friend_pizas:
    print('\t\t'+pizza)
    





    












