#10-1
filename = 'learning_python.txt'
with open(filename) as text_object:
	#(1)
	message = text_object.read()
	print(message.rstrip())

	#(2)
	# for line in text_object:
	# 	print(line.rstrip())

#(3)
# 	message = text_object.readlines()

# for line in message:
# 	print(line.rstrip())


#10-2
filename = 'learning_python.txt'

with open(filename) as change_text:
	for line in change_text:
		print(line.replace('can','can not').rstrip())
        

#10-3
# ~ filename = 'guest.txt'
# ~ with open(filename,'a') as text1:
    # ~ user = input("Please imout your name: ")
    # ~ text1.write(user + '\n')


#10-4 
# ~ filename = 'guesst_book.txt'
# ~ with open(filename,'a') as text2:
    # ~ while True:
        # ~ name = input("please input your name(enter 'q' to quit): ")
        # ~ if name == 'q':
            # ~ break
        # ~ else:
            # ~ print("hello " + name.title())
            # ~ text2.write(name + " has come. \n")


#10-6 and 10-7
'''加法運算檢錯'''

# print("Give me two nums, and I will add them")
# print("Enter 'q' to quit")

# while True:
#     try:
#         first_num = input("\nFirst number: ")
#         if first_num == 'q':
#             break
#         num_1 = int(first_num)
#     except ValueError:
#         print("you shuld input number !")
#         continue
#     try:    
#         second_num = input("\nSecond number: ")
#         if second_num ==  'q':
#             break
#         num_2 = int(second_num)
#     except ValueError:
#         print("you shuld input number !")
#         continue
#     answer = int(first_num) + int(second_num)
#     print(answer)

#10-10
'''計算某個單詞的數目'''
filename = "alice.txt"

with open(filename) as obj:
    lines = obj.readlines()

'''轉化爲字符串'''
pi_string = ''
for line in lines:
    pi_string += line.strip()

'''計算＇the＇的數量'''
num = pi_string.count('The')
print(str(num))


