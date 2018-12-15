#建立一个函数
print('\n一、')
add = lambda x, y :x + y
print(add(1, 2))
print('\n二、')

#map() 第一个参数为函数，第二个为对象列表

def add2(x):
    return x+2
#让列表里的每个数都执行函数运算，并得出结果，并且可以用list()进行强制转化为列表形式输出
text = list(map(add2, [1, 2, 3, 4]))
print(text)
# map = list(map(lambda x : x+2, [1, 2, 3, 4]))
print('\n三、')

#filter()第一个参数为函数，第二个为对象列表

a = [1, 2, 3, 4, 5, 6, 7, 8]
#让a里边的每一个值都除以2并且把能整除的数存起来
#并且可以用list()进行强制转化为列表形式输出
filter_text = list(filter(lambda x: x%2==0, a))
print(filter_text)

print('\n四')


import random
#生成随机数
'''
print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4))  # 产生1.1 到 5.4 之间的随机浮点数区间可以不是整数
print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数
'''
#
r1 = []
for num in range(50):# 循环50次
    r1.append(random.randint(1,10))# 生成1~10的随机数
print(r1)

#生成一个产生 0 到 1 之间的随机浮点数
r2 = []
r2.append(random.random())
print(r2)


#生成一个不重复的随机列表
r3 = []
'''函数介绍：

sample(seq, n) 从序列seq中选择n个随机且独立的元素；
'''
r3 =  random.sample(range(1, 101), 50)

print(r3)