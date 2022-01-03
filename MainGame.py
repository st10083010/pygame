# space shooting game

import random
import pygame
from pygame.constants import HAT_RIGHTUP
import Rock
import Bullet
import os
import drawText
import Explosion
import Items


FPS = 60

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (0, 255, 0)
BLACK_LAYER = (0, 0, 0)

TITLE = "GAME"


pygame.init()  # 遊戲初始化
pygame.mixer.init()  # 將音效模組初始化

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 解析度(視窗大小 tuple)
pygame.display.set_caption(TITLE)  # 標題
clock = pygame.time.Clock()  # 對時間進行管理與操控

# 圖片
backgroundImage = pygame.image.load(os.path.join(
    "image", "background.png")).convert()  # 先初始化才能載入圖片 # convert()將圖片轉為PYGAME較容易讀取的格式

playerImage = pygame.image.load(
    os.path.join("image", "player.png")).convert()

playerLivesIcon = pygame.transform.scale(playerImage, (25, 19))
playerLivesIcon.set_colorkey(BLACK_LAYER)

pygame.display.set_icon(playerLivesIcon)
# 音效
shootSound = pygame.mixer.Sound(os.path.join(
    "sound", "shoot.wav"))
laserSound = pygame.mixer.Sound(os.path.join("sound", "pow0.wav"))
shieldSound = pygame.mixer.Sound(os.path.join("sound", "pow1.wav"))

# 音樂
pygame.mixer.music.load(os.path.join("sound", "background.ogg"))
pygame.mixer.music.play(-1)  # play(播放幾次，-1 = 循環撥放)
pygame.mixer.music.set_volume(0.5)  # set_volume(傳入0~1，音量大小)


dropRate = 0.1  # 掉寶率
shieldEffect = 20  # 護盾回血量


def newRock():
    r = Rock.Rock()
    allSprites.add(r)
    rocksGroup.add(r)


def draw_mainMenu():
    screen.blit(backgroundImage, (0, 0))  # blit(畫的東西, 畫的位置)
    gameName = '太空生存戰'
    controllText1 = "「←/→」或「A/D」: 控制左右移動"
    controllText2 = "空白鍵(Space): 發射子彈"
    how_to_start = "按任意鍵開始遊戲"
    drawText.draw_text_forCHT(screen, gameName, 64,
                              WIDTH/2, HEIGHT/4 - 30)
    drawText.draw_text_forCHT(screen, controllText1, 30,
                              WIDTH/2, HEIGHT/2)
    drawText.draw_text_forCHT(screen, controllText2, 30,
                              WIDTH/2, HEIGHT/2 - 45)
    drawText.draw_text_forCHT(screen, how_to_start, 22,
                              WIDTH/2, HEIGHT*3/4)
    pygame.display.update()

    waiting = True
    while waiting:
        clock.tick(FPS)
        # 1秒鐘之內最多被執行10次(FPS)

        # 取得輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYUP:
                # KEYDOWN -> 按下的瞬間觸發；KEYUP -> 按下後放開按鍵才觸發
                waiting = False
                return False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # 引入預設函式

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
        self.health = 100  # 最大血量
        self.lives = 3  # 總生命值
        self.hidden = False  # 開局是否隱藏飛船
        self.hideTime = 0  # 隱藏時間
        self.laser = 1  # 子彈等級
        self.laserTime = 0  # 吃到閃電的時間

    def update(self):
        currently_time = pygame.time.get_ticks()
        if self.laser > 1 and currently_time - self.laserTime > 5000:  # 5000毫秒
            self.laser -= 1
            self.laserTime = currently_time

        if self.hidden and currently_time - self.hideTime > 3000:  # 3000毫秒
            # 經過一秒後將玩家(飛船)顯示出來)
            self.hidden = False
            self.rect.centerx = WIDTH/2  # 初始座標 左上角為(0, 0) 正中央寫法
            self.rect.bottom = HEIGHT - 20

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
        if not(self.hidden):
            if self.laser == 1:
                bullet = Bullet.Bullet(self.rect.centerx, self.rect.top)
                allSprites.add(bullet)
                bulletsGroup.add(bullet)
                shootSound.play()
            elif self.laser == 2:
                bullet1 = Bullet.Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet.Bullet(self.rect.right, self.rect.centery)
                allSprites.add(bullet1)
                allSprites.add(bullet2)
                bulletsGroup.add(bullet1)
                bulletsGroup.add(bullet2)
                shootSound.play()
            elif self.laser >= 3:
                bullet1 = Bullet.Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet.Bullet(self.rect.right, self.rect.centery)
                bullet3 = Bullet.Bullet(self.rect.centerx, self.rect.top)
                allSprites.add(bullet1)
                allSprites.add(bullet2)
                allSprites.add(bullet3)
                bulletsGroup.add(bullet1)
                bulletsGroup.add(bullet2)
                bulletsGroup.add(bullet3)
                shootSound.play()

    def hide(self):
        self.hidden = True
        self.hideTime = pygame.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT+500)  # 將飛船移出視窗外

    def laser_up(self):
        self.laser += 1
        self.laserTime = pygame.time.get_ticks()


mainMenu = True
# game_over_screen = False
running = True

while running:
    if mainMenu:
        iscolse = draw_mainMenu()
        if iscolse == True:
            break
        mainMenu = False
        allSprites = pygame.sprite.Group()  # 建立群組，群組內的物件通通會被一起控制
        rocksGroup = pygame.sprite.Group()
        bulletsGroup = pygame.sprite.Group()
        itemsGroup = pygame.sprite.Group()

        score = 0  # 起始分數
        player = Player()
        allSprites.add(player)

        for rocks in range(6):  # 石頭數量
            newRock()

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
        expl = Explosion.Explosion(
            hit.rect.center, 'bigbooms')
        allSprites.add(expl)
        if random.random() < dropRate:
            itemsDrop = Items.Power(hit.rect.center)
            allSprites.add(itemsDrop)
            itemsGroup.add(itemsDrop)

        newRock()

    # 傷害判斷(石頭是否與飛船相撞)
    isRockShip = pygame.sprite.spritecollide(
        player, rocksGroup, True, pygame.sprite.collide_circle)  # 當參數1碰撞到參數2時，是否將參數2刪除；參數4:預設碰撞面積為矩形
    # exitGame = pygame.key.get_pressed() # or exitGame[pygame.K_ESCAPE]

    for damage in isRockShip:  # 判斷是否有值，有值的時候將遊戲關閉
        newRock()
        player.health -= (int(damage.radius) - 10)
        expl = Explosion.Explosion(damage.rect.center, 'smallbooms')
        allSprites.add(expl)

        if player.health <= 0:
            dieExplosion = Explosion.Explosion(player.rect.center, 'player')
            allSprites.add(dieExplosion)
            Explosion.dieSound.play()
            player.lives -= 1
            player.health = 100
            player.hide()  # 將玩家(飛船)短暫隱藏

    # 道具判斷(道具是否與飛船相撞)
    isItemShip = pygame.sprite.spritecollide(player, itemsGroup, True)
    for bonus in isItemShip:
        if bonus.type == 'shield':
            player.health += shieldEffect
            if player.health > 100:
                player.health = 100
            shieldSound.play()
        elif bonus.type == 'laser_power':
            player.laser_up()
            laserSound.play()

    if player.lives == 0 and not(dieExplosion.alive()):
        # 當玩家生命值歸零且死亡動畫跑完時
        mainMenu = True

    # 畫面顯示------------------------------------------------
    screen.fill(BACKGROUND_COLOR)  # RGB(tuple)
    screen.blit(backgroundImage, (0, 0))  # blit(畫的東西, 畫的位置)
    allSprites.draw(screen)  # 把玩家畫到螢幕上
    drawText.draw_text(screen, ("Score: " + str(score)),
                       25, WIDTH/2, 10)  # 分數顯示
    drawText.draw_health(screen, player.health, 8, 15)
    drawText.draw_lives(screen, player.lives, playerLivesIcon, WIDTH - 100, 15)
    pygame.display.update()


pygame.quit()
