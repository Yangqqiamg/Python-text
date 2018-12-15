#one
people=['joke', 'xiaoming', 'joe', 'whinte', 'mary']
print(people[1:4])  # will show ['xiaoming', 'joe', 'whinte']


#two
print(people[:])    # will show the lists same as the people

#three
print(people[-2:])  #will show ['whinte', 'mary']

#four
print('here are the member lists :')
for num in people[:5]:
    print('\t\t\t'+num)

#five
member=people[:]
people.append('mike')
member.remove('joe')
print(people)
print(member)



