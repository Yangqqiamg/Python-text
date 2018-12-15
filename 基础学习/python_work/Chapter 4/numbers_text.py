#one
for num in range(1,10):    # means 1 to 9
	print(num)

#two
nums=list(range(1,5))
print(nums)

print(list(range(1,9)))     # will show [1,2,3,4,5,6,7,8]

#three
new_nums=list(range(1,9,3))
print(new_nums) #will show [1,4,7]

#four
squares=[]
for num in range(1,6):
	square=num**2   # means 1*1 2*2 3*3 4*4 5*5
	squares.append(square)
print(squares)      # will show [1,4,9,16,25]

#five
nums=[1,2,3,4,5,6,7,8,9,11,5,468,0]
print(min(nums))
print(max(nums))
print(sum(nums))

#six
squares=[num**2 for num in range(1,6)]
print(squares)	# will show [1,4,9,16,25]


