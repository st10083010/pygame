from math import ceil
import pygame
import os

pygame.mixer.init()  # 將音效模組初始化

dieSound = pygame.mixer.Sound(os.path.join(
    "sound", "rumble.ogg"))

BLACK_LAYER = (0, 0, 0)

bigBoomSize = (75, 75)
smallBoomSize = (30, 30)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)  # 引入預設函式
        global explosionAnimation
        explosionAnimation = {'bigbooms': [], 'smallbooms': [], 'player': []}
        for i in range(9):
            explosionIMG = pygame.image.load(os.path.join(
                "image", "expl{}.png").format(i)).convert()
            explosionIMG.set_colorkey(BLACK_LAYER)
            explosionAnimation['bigbooms'].append(
                pygame.transform.scale(explosionIMG, bigBoomSize))
            explosionAnimation["smallbooms"].append(
                pygame.transform.scale(explosionIMG, smallBoomSize))

            playerExplosionIMG = pygame.image.load(os.path.join(
                "image", "player_expl{}.png").format(i)).convert()
            playerExplosionIMG.set_colorkey(BLACK_LAYER)
            explosionAnimation["player"].append(playerExplosionIMG)

    # 將圖片引入，寫個字典存放大/小爆炸的LIST，接著把圖片去背(?)，放入大/小爆炸的LIST
        self.size = size
        self.image = explosionAnimation[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()  # 記錄圖片最後更新的時間(從初始化到現在所經過的毫秒數)
        self.frame_rate = 100  # 至少要經過幾毫秒才會更新到下一張圖片

    def update(self):
        now = pygame.time.get_ticks()  # 這裡被執行的時間
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosionAnimation[self.size]):
                self.kill()
            else:
                self.image = explosionAnimation[self.size][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
