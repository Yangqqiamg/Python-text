#one
message = input("please input a num: ")
print(message)

#two
name = input("please enter your name: ")
print("hello! " + name + ".")

#three
prompt = "if you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(name)

#four
age = input("How old are you ?")
age = int(age)
print(age >= 18)

#five
num = input("Iput a number, I will tell you if it's even or odd: ")
num = int(num)
if num %2 == 0:
    print("The " + str(num) + " is even .")
else:
    print("The " + str(num) + " is odd .")

# ~ #six
count_num = 1
while count_num <= 6:
    print(str(count_num))
    count_num += 1


# ~ #seven
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""

active = True
while active:
    message = input(prompt)

    if message != 'quit':
        print(message)
    else:
        active = False
while True:
    message = input(prompt)
    
    if message == 'quit':
        break
    else:
        print(message)

# ~ #eight
count_num = 0
while count_num < 10:
    count_num += 1
       
    if count_num % 2 == 0:
        continue
    else:
        print(count_num)
        
#nine
first_users = ['mike','joe','mary']
old_users = []

while first_users:
    old_user = first_users.pop()
    
    print("first user : " + old_user)
    old_users.append(old_user)

print("\nThey had become old user :")
for old_user in old_users:
    print(old_user)

#ten
pets = ['cat','dog','cat','fish','bird','fox']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

#eleven
responses = {}

falg = True

while falg :
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb ? ")
    
    responses[name] = response
    
    repeat = input("Whould you want to let anthor person respond?(y/n)")
    if repeat == 'n':
        falg = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " like to climb " + response)











