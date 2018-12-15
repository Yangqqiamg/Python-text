from random import choice

class RandomWalk():
    """一个生成随机漫步的类"""

    #默认值进行5000次漫步
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        #所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        #不断漫步,直到列表x_values达到指定的长度
        while len(self.x_values) < self.num_points:

            #决定前进方向以及沿着这个方向前进的距离
            x_direction = choice([1, -1]) #选择向左向右移动
            x_distance = choice([0, 1, 2, 3, 4,]) #选择移动的步数
            x_step = x_direction * x_distance #确定x的坐标

            y_direction = choice([1, -1]) #选择向左向右移动
            y_distance = choice([0, 1, 2, 3, 4,]) #选择移动的步数
            y_step = y_direction * y_distance #确定y的坐标

            #拒绝原地踏步
            if x_step == 0 and y_step == 0 :
                continue # 继续执行

            #计算下一个点的x和y值
            #[-1]  则为列表的倒数1的值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)