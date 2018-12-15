import json

"""方法一"""

# filename = 'favo_num.json'
# try:
# 	with open(filename) as num_obj:
# 		num = json.load(num_obj)
# except FileNotFoundError:
# 	num = input("please input your favorite number: ")
# 	with open(filename,'w') as	num_obj:
# 		json.dump(num,num_obj)
# 		print("thanks! I remember it. ")
# else:
# 	print("I know your favorite number is " + str(num) + "!")


'''方法二'''

def get_num():
	num = input("please input your favorite number: ")
	filename = 'favo_num.json'
	with open(filename,'w') as	num_obj:
		json.dump(num,num_obj)
	return num

def show_num():
	filename = 'favo_num.json'
	try:
		with open(filename) as num_obj:
			num = json.load(num_obj)
	except FileNotFoundError:
		return None
	else:
		return num
	pass

def check_num():
	num = show_num()
	if num:
		print("I know your favorite number is " + str(num) + "!")
	else:
		num = get_num()
		print("thanks! I remember it. ")

    check_num()