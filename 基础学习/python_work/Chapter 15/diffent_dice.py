import pygal
from die import Die

#创建2个D6
die_1 = Die()
die_2 = Die(10)

#投几次骰子，将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析数据
frequencies = []
for value in range(1, die_1.num_sides+1+die_2.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 50000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
            '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add(' D10+D6', frequencies)
hist.render_to_file('die_visual.svg')
