import pygame
import os
import random


WIDTH = 800
HEIGHT = 600
BLACK_LAYER = (0, 0, 0)

itemSpeed = 3


class Power(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)  # 引入預設函式
        itemsImg = {}
        itemsImg['shield'] = pygame.image.load(
            os.path.join("image", "shield.png")).convert()
        itemsImg['laser_power'] = pygame.image.load(
            os.path.join("image", "gun.png")).convert()

        self.type = random.choice(['shield', 'laser_power'])
        self.image = itemsImg[self.type]
        self.image.set_colorkey(BLACK_LAYER)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = itemSpeed

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()
