"""散点图"""

#导入matplotlib中的pyplot模块用于绘图
import matplotlib.pyplot as plt

#指定两组列表,一个为y轴值,一个为x坐标
#x_values 生成一个1~1000的列表
#  list()  生成一个列表
#  range()  循环
#y_values 列表解析,根据x_values生成对应的平方数
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]


#函数scatter()  在每个x_values与y_values对应位置生成点,
#               s=20 指定点的大小
#               edgecolor='none' 删除数据点轮廓
#               c='red'       指定颜色   或:
#               c=(0, 0, 0.8) 分别表示红绿蓝的分量,0~1之间越大越浅
#               c=y_values, cmap=plt.cm.Blues  参数c设置成一个y值列表,参数cmap表
#                                              明使颜色.
#                             结果表示: y值小的显示为浅蓝色,大的显示为深蓝色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
             edgecolor='none', s=20)

#设置图表标题,并给坐标轴加上标签:
#  title()  设置标题格式:名字, 字体大小
#  xlabel()  设置x轴格式:名字, 字体大小
#  ylabel()  设置y轴格式:名字, 字体大小
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置坐标轴的取值范围
#axis()  [0, 1100, 0, 1100000]分别为x轴和y轴的最小值与最大值
plt.axis([0, 1100, 0, 1100000])

#设置刻度标记的大小:
#  tick_params()  axis='both'指定实参影响x,y轴上的刻度,设置刻度标记字体大小
#                 which一共3个参数['major' ， 'minor'，'both']
#                      默认是major表示主刻度，后面分布为次刻度及主次刻度都显示

plt.tick_params(axis='both', which='major', labelsize=14)

#函数show()  打开matplotlib 的图形查看器
plt.show()