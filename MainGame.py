# space shooting game

import pygame
from pygame.constants import HAT_RIGHTUP
import Rock
import Bullet
import os


FPS = 60

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (0, 255, 0)
BLACK_LAYER = (0, 0, 0)


pygame.init()  # 遊戲初始化

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 解析度(視窗大小 tuple)
pygame.display.set_caption("game")  # 標題
clock = pygame.time.Clock()  # 對時間進行管理與操控

backgroundImage = pygame.image.load(os.path.join(
    "image", "background.png")).convert()  # 先初始化才能載入圖片 # convert()將圖片轉為PYGAME較容易讀取的格式


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
        pygame.draw.circle(self.image, PLAYER_COLOR,
                           self.rect.center, self.redius)  # 將圖片畫出來(畫在哪，顏色，座標，半徑長)
        self.rect.centerx = WIDTH/2  # 初始座標 左上角為(0, 0) 正中央寫法
        self.rect.bottom = HEIGHT - 20

        self.speedx = 10  # X 軸速度控制

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


allSprites = pygame.sprite.Group()  # 建立群組，群組內的物件通通會被一起控制
rocksGroup = pygame.sprite.Group()
bulletsGroup = pygame.sprite.Group()

player = Player()
allSprites.add(player)

for rocks in range(6):  # 石頭數量
    r = Rock.Rock()
    allSprites.add(r)
    rocksGroup.add(r)


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
        r = Rock.Rock()
        allSprites.add(r)
        rocksGroup.add(r)

    isGameStop = pygame.sprite.spritecollide(
        player, rocksGroup, False, pygame.sprite.collide_circle)  # 當參數1碰撞到參數2時，是否將參數2刪除；參數4:預設碰撞面積為矩形
    if isGameStop:  # 判斷是否有值，有值的時候將遊戲關閉
        running = False
    # 畫面顯示------------------------------------------------
    screen.fill(BACKGROUND_COLOR)  # RGB(tuple)
    screen.blit(backgroundImage, (0, 0))  # blit(畫的東西, 畫的位置)
    allSprites.draw(screen)  # 把玩家畫到螢幕上
    pygame.display.update()


pygame.quit()
