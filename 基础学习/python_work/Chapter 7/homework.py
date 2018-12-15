#7-1
message = input("Please tell me what you want: ")
print("Let me see if I can find you a " + message.title())

#7-2
num = input("How many people are you have ? ")
num = int(num)
if num > 8:
    print("sorry we don't have desk. ")
else:
    print("Well coming please! ")

# ~ #7-3
num = input("please input a num : ")
num = int(num)
if num % 10 == 0:
    print("the " + str(num) + " ture")
else:
    print("the " + str(num) + " bad")


# ~ #7-4
prompt = "\nTell me something, and I will add in your pizza: "
prompt += "\nEnter 'quit' to end the program. "

while True:
    add = input(prompt)
    if add != 'quit':
        print("We will add " + add.title() + " in your pizza !")
    else:
        break


# ~ #7-5
message = "\nTell me your age :"
message += "\nEnter 'quit' to end the program. "

active = True
while active:
    age = input(message)
    age = int(age)
    if age < 3:
        print("you are free!")
    elif 3 <= age <=12:
        print("you should pay 10 $")
    else:
        print("you should pay 15 $")
        
#7-8 and 7-9
sandwich_orders = ['egg','beef','meat','beef','milk','beef']
finished_sandwiches = []
print("the beef had sell out!")
while 'beef' in sandwich_orders:
    sandwich_orders.remove('beef')
while sandwich_orders :
    sandwich = sandwich_orders.pop()
    print(sandwich + " is alraedy ! ")
    finished_sandwiches.append(sandwich)
    
print("\nAll sandwich has finished !")
for sandwich in finished_sandwiches:
    print(sandwich)

#7-10
message = '\nIf you want to visit one place in the world, where you go? '
message += "\nEnter 'quit' to end the program."
places = {}

while True:
    place = input(message)
    if place == 'quit':
        break
    name = input("\nwhat is your name?\nEnter 'quit' to end the program. ")
    if name == 'quit':
        break
    places[name] = place
    
for name,place in places.items():
        print('\n\n' + name + " like " + place)






















