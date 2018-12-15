import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    #初始pygame,设置和拼命屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))#游戏窗口尺寸
    pygame.display.set_caption("Alien Invasion")

    #创建一只飞船
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()

    #开始游戏的主循环
    while  True:
        gf.check_events(ai_settings, screen, ship, bullets)  #检测事件
        ship.update()              #更新飞船信息
        gf.update_bullets(bullets)  #对子弹进行处理
        gf.update_screen(ai_settings, screen, ship,bullets)  #更新屏幕

run_game()