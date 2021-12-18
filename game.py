# space shooting game

import pygame

FPS = 60
TITLE = pygame.display.set_caption("game")  # 標題
WIDTH = 800
HEIGHT = 600

backgroundColor = (200, 100, 50)

pygame.init()  # 遊戲初始化

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 解析度(視窗大小 tuple)
clock = pygame.time.Clock()  # 對時間進行管理與操控


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # 引入預設函式
        self.image = pygame.Surface((50, 40))  # 玩家面積
        self.image.fill((0, 255, 0))  # 玩家顏色
        self.rect = self.image.get_rect()  # 定位
        self.rect.center = (WIDTH/2, HEIGHT/2)  # 初始座標 左上角為(0, 0) 正中央寫法

    def update(self):
        self.rect.y += 3
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0


allSprites = pygame.sprite.Group()  # 建立群組，群組內的物件通通會被一起控制
player = Player()
allSprites.add(player)


running = True

while running:
    clock.tick(FPS)  # 1秒鐘之內最多被執行10次(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新遊戲
    allSprites.update()  # 執行allSprites中每個物件的update函式
    # 畫面顯示
    screen.fill(backgroundColor)  # RGB(tuple)
    allSprites.draw(screen)  # 把玩家畫到螢幕上
    pygame.display.update()


pygame.quit()
