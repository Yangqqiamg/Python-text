import matplotlib.pyplot as plt

from random_walk import RandomWalk

#只要程序活跃就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk实例, 并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk() #生成随机漫步坐标列表

    #设置绘图窗口的分辨率与尺寸
    plt.figure( dpi=128, figsize=(10, 6))

    #生成一个有num_points数目个数的列表
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=1)  #绘制散点图,按顺序着色深浅,删除黑色轮廓,大小为10

    #突出起点和终点
    plt.scatter(0, 0, c='green', edgecolor='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
         s=50) #显示列表中的最后一个点

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    #判断
    keep_running = input("Make it running again? (y/n)") #输入语句
    if keep_running == 'n': #如果是'n'就结束循环
        break