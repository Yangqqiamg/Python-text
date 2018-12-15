def print_modles(new_modles,finish_modles):
    while new_modles:
        finish_modle = new_modles.pop()
        print("printint_modle: " + finish_modle)
        finish_modles.append(finish_modle)

def show_modles(finish_modles):
    print("\nThe following modles have been printed: ")
    for finish_modle in finish_modles:
        print(finish_modle)

# ~ one = ['ddd','ggg','eee','hhh']
# ~ two = []

# ~ print_modles(one[:],two)#one[:] is copy from the one
# ~ show_modles(two)
# ~ print(one)
