name=['mike','joe','whinte']
print(name[0].title())
print(name[1].title())
print(name[2].title())

#[-1] means the last element
print(name[-1].title()) #will show whinte

#name[] the num is the lists place
message="This is my firend "+name[0].title()+"!"
print(message)

#name[]----change the first 'mike'to'joke'
name[0]='joke' 
print(name) #will show ['joke', 'joe', 'whinte']

#append()----add a new name 'mary' to the last
name.append('mary')
print(name) #will show ['joke', 'joe', 'whinte', 'mary']

#add a new name 'xiaoming' to '1' place
name.insert(1,'xiaoming')
print(name)  #will show ['joke', 'xiaoming', 'joe', 'whinte', 'mary']

#delete the "0" name
del name[0]
print(name) #will show ['xiaoming', 'joe', 'whinte', 'mary']

#pop----let a name to else place
popped_name=name.pop()
print(name) #will show ['xiaoming', 'joe', 'whinte']
print(popped_name)#will show  mary

best_name=name.pop(0) #pop(0) is xiaoming
message="my best friend is "+ best_name.title()
print(message)

#remove----
name=['mike','joe','whinte']
print(name)
name.remove('joe')
print(name) #will show ['mike', 'whinte']


