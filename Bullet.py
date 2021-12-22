import pygame
import os

WIDTH = 800
HEIGHT = 600
BLACK_LAYER = (0, 0, 0)
pygame.init()  # 遊戲初始化

bulletColor = (255, 215, 0)
bulletImage = pygame.image.load(os.path.join("image", "bullet.png")).convert()
bulletSpeed = -10


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # 引入預設函式
        self.image = pygame.Surface((10, 20))  # 圖像面積
        self.image.fill(bulletColor)  # 圖像顏色

        self.rect = self.image.get_rect()  # 定位
        self.rect.x = x  # 座標
        self.rect.y = y

        self.speedy = bulletSpeed  # Y 軸速度控制

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()  # 當條件達成，檢查所有Sprite群組，當有Bullet在裡面，就會把它移除
