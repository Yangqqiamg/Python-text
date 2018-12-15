import pygame
class Fang():
    def __init__(self, screen):
        self.screen = screen

        self.rect = pygame.Rect(0, 0 , 50, 50)

        self.rect.centery = self.screen.rect.centery
        self.rect.left = self.screen.rect.left

    def draw_fang(self):
        pygame.draw.rect(self.screen, self.rect)
