#one
user_list = []
# ~ user_list = ['jake','admin','mike','loe','mary']
if user_list == []:
    print ('we need to find sone users')
else:
    for user in user_list:
        if user == 'admin':
            print('hello admin,would you like to see a status report ?')
        
        print('hello!' + user.title())


#two
current_users = ['mike','joe','white','mary','lihua']
new_users = ['Mary','xiaoming','zhangliang', 'joe','admin']
for name in new_users:
    if name.lower() in current_users:
        print('sorry!' + name.title() + ' had been use , please uses another')
    else :
        print('you can use ' + name.title())


#three
nums = [1,2,3,4,5,6,7,8,9]
for num in nums:
    if num == 1:
        print(str(num) + 'st')
    elif num == 2:
        print(str(num) + 'nd')
    elif num == 3:
        print(str(num) + 'rd')
    else:
        print(str(num) + 'th')








