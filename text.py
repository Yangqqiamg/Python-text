names={'name':'Kevin','name2':'Tom'}
print ('hello {names[name]}  i am {names[name2]}'.format(names=names))
print('hello{0} i am {1}'.format('Kevin','Tom'))

data = {
    'id': '201514410',
    'name': 'job',
    'age': 21
}
print(tuple(data.values())*2)

for key in data:
    print(key)

def text():
    nmes={'name':'Kevin','name2':'Tom'}
    return nmes
