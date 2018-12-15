import pygal
from die import Die

#创建3个D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

#投几次骰子，将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

#分析数据
max_sides = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = []

for value in range(1, max_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [str(x) for x in range(1, max_sides+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add(' two D6', frequencies)
hist.render_to_file('die_visual.svg')
