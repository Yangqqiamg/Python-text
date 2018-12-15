import matplotlib.pyplot as plt
from random_walk import RandomWork

#如果处于活跃状态，就不断漫步
while True:
    #绘制一个实例，并将其包含的点都绘制出来
    rw = RandomWork(50000)
    rw.fill_walk()

    #设置绘图窗口的尺寸
    plt.figure(dpi=80, figsize =(10, 6))    #dpi为像素  figsize为长宽（英寸）

    point_number = list(range(rw.num_points))
    #plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.scatter(rw.x_values, rw.y_values,c=point_number, cmap = plt.cm.Blues,
        edgecolor='none', s=1)
    plt.title("hahaha", fontsize=24)

    #突出起点和终点
    plt.scatter(0, 0, c='green', edgecolor='none',s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolor='none',
         s=100)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break