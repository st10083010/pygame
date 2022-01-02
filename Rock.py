import pygame
import os
import random


WIDTH = 800
HEIGHT = 600
BLACK_LAYER = (0, 0, 0)

pygame.mixer.init()  # 將音效模組初始化
rockColor = (255, 90, 43)

rockExplosionSound = [
    pygame.mixer.Sound(os.path.join("sound", "expl0.wav")),
    pygame.mixer.Sound(os.path.join("sound", "expl1.wav"))
]


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # 引入預設函式
        # rockImage = pygame.image.load(
        #     os.path.join("image", "rock.png")).convert()
        rockImgList = []
        for i in range(7):
            rockImgList.append(pygame.image.load(
                os.path.join("image", "rock{}.png").format(i)).convert())

        self.imageOrigin = random.choice(rockImgList)
        self.imageOrigin.set_colorkey(BLACK_LAYER)  # set_colorkey(去除黑色部分)
        self.image = self.imageOrigin.copy()  # 石頭面積

        self.rect = self.image.get_rect()  # 定位
        self.redius = self.rect.width * 0.8 / 2  # 碰撞圓面積半徑
        # pygame.draw.circle(self.image, rockColor,
        #                    self.rect.center, self.redius)  # 將圖片畫出來(畫在哪，顏色，座標，半徑長)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)  # 座標
        self.rect.y = random.randrange(-180, -100)

        self.speedy = random.randrange(2, 5)  # Y 軸速度控制
        self.totalDegress = 0  # 開始角度
        self.rotDegress = random.randrange(-5, 5, 2)  # 每次旋轉的角度

    def rotate(self):
        self.totalDegress += self.rotDegress
        self.totalDegress = self.totalDegress % 360
        self.image = pygame.transform.rotate(
            self.imageOrigin, self.totalDegress)  # 內建旋轉圖片函式(圖片, 角度)

        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)  # 座標
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)  # Y 軸速度控制
