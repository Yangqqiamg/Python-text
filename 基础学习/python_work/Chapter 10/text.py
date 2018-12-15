#one
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

#two
filename = 'pi_digits.txt'

with open(filename) as file_object1:
	for line in file_object1:
		print(line.rstrip())


#three
filename = 'pi_digits.txt'
with open(filename) as file_object2:
	lines = file_object2.readlines()

for line in lines:
	print(line.rstrip())

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#four
filename = 'pi_million_digits.txt'
with open(filename) as file_object3:
		lines = file_object3.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))

#five
filename = 'pi_million_digits.txt'
with open(filename) as file_object4:
		lines = file_object4.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()


# birth = input("Enter your birthday, in the form mmddyy: ")
# if birth in pi_string:
#     print("your birthday appears in the first million digit of pi!")
# else:
#     print("sorry! not in here")

#six
filename = 'programing.txt'
# with open(filename,'w') as file_text:
# 	file_text.write("I can write it !\n")
# 	file_text.write('I love it !\n')

with open(filename,'a') as file_text1:
	file_text1.write("I also love other things!\n")

#seven
try:
	print(5/0)
except ZeroDivisionError:
	print("you can mot divide bo zero")

#eight
# print("Give me two nums, and I will divide them")
# print("Enter 'q' to quit")

# while True:
# 	first_num = input("\nFirst number: ")
# 	if first_num == 'q':
# 		break
# 	second_num = input("\nSecond number: ")
# 	if second_num ==  'q':
# 		break
# 	try:
# 		answer = int(first_num)/int(second_num)
# 	except ZeroDivisionError:
# 		print("you can not divide by 0")
# 	else:
# 		print(answer)

#nine
def count_words(filename):
	'''計算一個文件的大致單詞數'''
	try:	
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass#直接繼續執行不反饋
		
		# msg = "Sorry, the file " + filename + " dose not found"
		# print(msg)
	else:
		words = contents.split()#以空格爲分割符，拆分，並且存到一個列表裏
		num_words = len(words)
		print("the file " + filename + " has about " + str(num_words) + " words.")

# count_words('alice.txt')

filenames = ['alice.txt', 'aisfwf.txt', 'moby_dict.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)