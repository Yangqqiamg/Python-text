#one
guest=['xiaohong','xiaoming','lihua']
message="guest:\n\t"+guest[0]+'\n\t'+guest[1]+'\n\t'+guest[2]
print(message.title())

#two
new_guest=guest.pop(0)
print('\n'+new_guest+" can't participate the dinner")
guest.insert(0,'zhangliang')
message="guest:\n\t"+guest[0]+'\n\t'+guest[1]+'\n\t'+guest[2]
print(message.title())

#three
print('\neveryone I found a new bigger dest!')
guest.insert(0,'yaoming')
guest.insert(2,'zengpeng')
guest.append('chenhua')
message="guest:\n\t"+guest[0]+'\n\t'+guest[1]+'\n\t'+guest[2]+'\n\t'+guest[3]+'\n\t'+guest[4]+'\n\t'+guest[5]
print(message.title())

#four
print('\nsorry everyone I only can invite two people\n')
out_guest=guest.pop(1)
print("dear "+out_guest+":"+"\n\tsorry I can't invite you")
out_guest=guest.pop(0)
print("dear "+out_guest+":"+"\n\tsorry I can't invite you")
out_guest=guest.pop(0)
print("dear "+out_guest+":"+"\n\tsorry I can't invite you")
out_guest=guest.pop(0)
print("dear "+out_guest+":"+"\n\tsorry I can't invite you")

print("dear "+guest[0]+":"+"\n\tI hope you can participate to my dinner!")
print("dear "+guest[1]+":"+"\n\tI hope you can participate to my dinner!")

del guest[0]
del guest[0]
print(guest)

