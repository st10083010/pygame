import pygame
import os
import random


WIDTH = 800
HEIGHT = 600
BLACK_LAYER = (0, 0, 0)
pygame.init()  # 遊戲初始化

rockColor = (139, 90, 43)
rockImage = pygame.image.load(os.path.join("image", "rock.png")).convert()


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # 引入預設函式
        self.image = rockImage  # 石頭面積
        self.image.set_colorkey(BLACK_LAYER)

        self.rect = self.image.get_rect()  # 定位
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)  # 座標
        self.rect.y = random.randrange(-100, -40)

        self.speedy = random.randrange(2, 10)  # Y 軸速度控制

    def update(self):
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)  # 座標
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)  # Y 軸速度控制
