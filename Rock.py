import pygame
import os
import random


WIDTH = 800
HEIGHT = 600
BLACK_LAYER = (0, 0, 0)


rockColor = (255, 90, 43)


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # 引入預設函式
        rockImage = pygame.image.load(
            os.path.join("image", "rock.png")).convert()
        self.image = rockImage  # 石頭面積
        self.image.set_colorkey(BLACK_LAYER)  # set_colorkey(去除黑色部分)

        self.rect = self.image.get_rect()  # 定位
        self.redius = self.rect.width * 0.8 / 2  # 碰撞圓面積半徑
        pygame.draw.circle(self.image, rockColor,
                           self.rect.center, self.redius)  # 將圖片畫出來(畫在哪，顏色，座標，半徑長)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)  # 座標
        self.rect.y = random.randrange(-100, -40)

        self.speedy = 1  # random.randrange(2, 10)  # Y 軸速度控制

    def update(self):
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)  # 座標
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)  # Y 軸速度控制
