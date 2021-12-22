import pygame
import random

WIDTH = 800
HEIGHT = 600


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # 引入預設函式
        self.image = pygame.Surface((30, 40))  # 石頭面積
        self.image.fill((0, 0, 0))  # 石頭顏色

        self.rect = self.image.get_rect()  # 定位
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)  # 座標
        self.rect.y = random.randrange(-100, -40)

        self.speedy = 5  # Y 軸速度控制

    def update(self):
        self.rect.y += self.speedy
