import sys

import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 500))#窗口大小
    pygame.display.set_caption("Moving Game")#窗口名字

    bg_color = (200, 200, 200)
    #开始游戏
    while True:
        for event in pygame.event.get():    #检测鼠标和键盘事件
            if event.type == pygame.QUIT:   #如果按下关闭
                sys.exit()                  #执行退出窗口

        screen.fill(bg_color)               #每次循环都重绘屏幕
        pygame.display.flip()               #让最近绘制的窗口可见

run_game()