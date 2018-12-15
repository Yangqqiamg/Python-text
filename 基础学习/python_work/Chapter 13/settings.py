class Settings():
    '''存储《外星人入侵》的所有设置的类'''

    def __init__(self):
        '''初始化游戏的静态设置'''
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        #飞船的设置
        self.ship_limit = 1
        #子弹设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 4
        #外星人的设置
        self.fleet_drop_speed = 10          #向下移动速度


        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.5
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed_factor = 0.8
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.5       #向右移动速度

        #fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

        #计分
        self.alien_point = 50

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_point = int(self.alien_point * self.score_scale)
