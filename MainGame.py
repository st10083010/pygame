# space shooting game

import pygame
import Rock
import Bullet


FPS = 60
TITLE = pygame.display.set_caption("game")  # 標題
WIDTH = 800
HEIGHT = 600

backgroundColor = (200, 100, 50)
playerColor = (0, 255, 0)


pygame.init()  # 遊戲初始化

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 解析度(視窗大小 tuple)
clock = pygame.time.Clock()  # 對時間進行管理與操控


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # 引入預設函式
        self.image = pygame.Surface((50, 40))  # 玩家面積
        self.image.fill(playerColor)  # 玩家顏色

        self.rect = self.image.get_rect()  # 定位
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


allSprites = pygame.sprite.Group()  # 建立群組，群組內的物件通通會被一起控制
player = Player()
allSprites.add(player)

for rocks in range(10):  # 石頭數量
    r = Rock.Rock()
    allSprites.add(r)


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

    # 更新遊戲
    allSprites.update()  # 執行allSprites中每個物件的update函式
    # 畫面顯示
    screen.fill(backgroundColor)  # RGB(tuple)
    allSprites.draw(screen)  # 把玩家畫到螢幕上
    pygame.display.update()


pygame.quit()
