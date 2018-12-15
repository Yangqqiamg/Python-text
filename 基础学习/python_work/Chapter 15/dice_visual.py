import pygal
import matplotlib.pyplot as plt
from die import Die

#创建2个D6
die_1 = Die(8)
die_2 = Die(8)

#投几次骰子，将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析数据
frequencies = []
for value in range(1, die_1.num_sides+1+die_2.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [str(x) for x in range(1, die_1.num_sides+1+die_2.num_sides)]

point_num = list(range(1000))
plt.scatter(range(1,1001), results, c=point_num, cmap=plt.cm.Greens,
     edgecolor='none', s=40)
#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"

# hist.add(' two D6', frequencies)
# hist.render_to_file('die_visual.svg')
