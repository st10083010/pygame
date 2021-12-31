# space shooting game

import random
import pygame
from pygame.constants import HAT_RIGHTUP
import Rock
import Bullet
import os
import drawText


FPS = 60

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (0, 255, 0)
BLACK_LAYER = (0, 0, 0)


pygame.init()  # 遊戲初始化
pygame.mixer.init()  # 將音效模組初始化

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 解析度(視窗大小 tuple)
pygame.display.set_caption("game")  # 標題
clock = pygame.time.Clock()  # 對時間進行管理與操控

# 圖片
backgroundImage = pygame.image.load(os.path.join(
    "image", "background.png")).convert()  # 先初始化才能載入圖片 # convert()將圖片轉為PYGAME較容易讀取的格式

# 音效
shootSound = pygame.mixer.Sound(os.path.join(
    "sound", "shoot.wav"))

# 音樂
pygame.mixer.music.load(os.path.join("sound", "background.ogg"))
pygame.mixer.music.play(-1)  # play(播放幾次，-1 = 循環撥放)
pygame.mixer.music.set_volume(0.5)  # set_volume(傳入0~1，音量大小)

score = 0


def newRock():
    r = Rock.Rock()
    allSprites.add(r)
    rocksGroup.add(r)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # 引入預設函式
        playerImage = pygame.image.load(
            os.path.join("image", "player.png")).convert()

        self.image = pygame.transform.scale(
            playerImage, (50, 50))  # scale(圖片, (大小))

        self.image.set_colorkey(BLACK_LAYER)  # set_colorkey(去除黑色部分)

        self.rect = self.image.get_rect()  # 定位
        self.redius = 30  # 碰撞圓面積半徑
        # pygame.draw.circle(self.image, PLAYER_COLOR,
        #                    self.rect.center, self.redius)  # 將圖片畫出來(畫在哪，顏色，座標，半徑長)
        self.rect.centerx = WIDTH/2  # 初始座標 左上角為(0, 0) 正中央寫法
        self.rect.bottom = HEIGHT - 20

        self.speedx = 10  # X 軸速度控制
        self.health = 100  # 血量

    def update(self):
        keyPressed = pygame.key.get_pressed()  # 回傳boolean值 當鍵盤有按鍵被按下去 回傳True
        if keyPressed[pygame.K_RIGHT] or keyPressed[pygame.K_d]:  # 右鍵是否觸發(方向鍵)
            self.rect.x += self.speedx
        if keyPressed[pygame.K_LEFT] or keyPressed[pygame.K_a]:  # 左鍵是否觸發(方向鍵)
            self.rect.x -= self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet.Bullet(self.rect.centerx, self.rect.top)
        allSprites.add(bullet)
        bulletsGroup.add(bullet)
        shootSound.play()


allSprites = pygame.sprite.Group()  # 建立群組，群組內的物件通通會被一起控制
rocksGroup = pygame.sprite.Group()
bulletsGroup = pygame.sprite.Group()

player = Player()
allSprites.add(player)


for rocks in range(6):  # 石頭數量
    newRock()


running = True

while running:
    clock.tick(FPS)  # 1秒鐘之內最多被執行10次(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # 更新遊戲-------------------------------------------------
    allSprites.update()  # 執行allSprites中每個物件的update函式
    hits = pygame.sprite.groupcollide(
        rocksGroup, bulletsGroup, True, True)  # return dictionary
    for hit in hits:
        random.choice(Rock.rockExplosionSound).play()
        score += int((hit.redius) + 10)  # 分數管理
        newRock()

    isGameStop = pygame.sprite.spritecollide(
        player, rocksGroup, True, pygame.sprite.collide_circle)  # 當參數1碰撞到參數2時，是否將參數2刪除；參數4:預設碰撞面積為矩形
    # exitGame = pygame.key.get_pressed() # or exitGame[pygame.K_ESCAPE]
    for damage in isGameStop:  # 判斷是否有值，有值的時候將遊戲關閉
        newRock()
        player.health -= (int(damage.radius) - 10)
        if player.health <= 0:
            running = False
    # 畫面顯示------------------------------------------------
    screen.fill(BACKGROUND_COLOR)  # RGB(tuple)
    screen.blit(backgroundImage, (0, 0))  # blit(畫的東西, 畫的位置)
    allSprites.draw(screen)  # 把玩家畫到螢幕上
    drawText.draw_text(screen, ("Score: " + str(score)),
                       25, WIDTH/2, 10)  # 分數顯示
    drawText.draw_health(screen, player.health, 8, 15)
    pygame.display.update()


pygame.quit()
