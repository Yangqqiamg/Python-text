#12-1  and 12-2
import sys

import pygame
from ship import Ship


def run_game():
    #初始pygame,设置和拼命屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((500, 300))#游戏窗口尺寸
    pygame.display.set_caption("Test Invasion")
    bg_color = (0,0,255)

    new_ship = Ship(screen)
    while True:
        '''监视键盘和鼠标的事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        new_ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()