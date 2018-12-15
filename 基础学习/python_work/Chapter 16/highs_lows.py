import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)          #把读取的文档给reader
    header_low = next(reader)       #读取第一行信息
    #print(header_low)

    # #获取索引及其值（enumerate函数）
    # for index, column_header in enumerate(header_low):
    #     print(index, column_header)

    dates, highs, lows = [], [], []       #创建三个列表
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))  ##dpi为像素  figsize为长宽（英寸）
plt.plot(dates, highs, c='red', linewidth=1, alpha=0.5)  #导入数据 和 选择颜色
plt.plot(dates, lows, c='blue', linewidth=1, alpha=0.5)  #alpha 为透明度
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)#填充颜色

#设置图形格式
plt.title("aaa", fontsize=24)
plt.xlabel('', fontsize=16)
plt.xlim(dates[0],dates[-1])           #设置x轴坐标范围
fig.autofmt_xdate()                    #让x轴标签倾斜显示
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()