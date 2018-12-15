"""折线图"""

#导入matplotlib中的pyplot模块用于绘图
import matplotlib.pyplot as plt

#指定两组列表,一个为y轴值,一个为x坐标
squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]

#使用函数plot()绘制出以input_values列表为x轴,squares为y值的有关折线图
#  linewidth=5  指定线宽为5
plt.plot(input_values, squares, linewidth=5)

#设置图表标题,并给坐标轴加上标签:
#  title()  设置标题格式:名字, 字体大小
#  xlabel()  设置x轴格式:名字, 字体大小
#  ylabel()  设置y轴格式:名字, 字体大小
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小:
#  tick_params()  axis='both'指定实参影响x,y轴上的刻度,设置刻度标记字体大小
plt.tick_params(axis='both', labelsize=14)

#函数show()打开了matplotlib的查看器显示图表
plt.show()