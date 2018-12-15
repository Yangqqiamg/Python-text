#one
'''數據存儲與讀取'''
import json

numbers = [2, 6, 7, 1, 8, 5, 7]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj)

filename = 'numbers.json'
with open(filename) as f_obj:
	num = json.load(f_obj)

print(num)

#two
# import json

# filename = 'username.json'
# try:
# 	with open(filename) as f_obj:
# 		username = json.load(f_obj)
# except FileNotFoundError:
# 	username = input("What is your name ? :")
# 	with open(filename,'w') as f_obj:
# 		json.dump(username,f_obj)
# 		print("We'll remember you when  you come back, " + username + ' ! ')
# else:
# 	print("wellcome back!, " + username)

import json
def get_stored_username():
	'''如果存儲了用戶名，就獲取他'''
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username	


def get_new_name():
	'''提示用戶輸入名字'''
	username = input("What is your name ? :")
	filename = 'username.json'
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
	return username

def greet_user():
	'''問候用戶，並指出其名字'''
	filename = 'username.json'
	username = get_stored_username()
	if username:
		check_name = input("you name is:" + username + ",right? (Enter 'y' or 'n'): ")
		if check_name == 'y':
			print("wellcome back!, " + username)
		elif check_name == 'n':
			username = get_new_name()
			print("We'll remember you when  you come back, " + username + ' ! ')
	else:
		username = get_new_name()
		print("We'll remember you when  you come back, " + username + ' ! ')

greet_user()