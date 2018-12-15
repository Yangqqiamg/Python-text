class Employee():
    def __init__(self,first,last,money):
        self.first = first
        self.last = last
        self.money = money

    def give_raise(self,add_money=5000):
        full_name = self.first + ' ' + self.last
        self.money += add_money
        # print("name: " + full_name.title())
        # print("money: " + str(new_money) + '$\n')

        pass

# test = Employee('joe','dig',500)
# test.give_raise()