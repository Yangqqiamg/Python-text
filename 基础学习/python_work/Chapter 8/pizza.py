def make_new_pizza(size,*toppings):
	print("makeing a " + str(size) + 
		" - pizza with the following toppings:")
	for pizza in toppings:
		print('-' + pizza)
	pass
