# space shooting game

import pygame

FPS = 60
backgroundColor = (200, 100, 50)
width = 800
height = 600

pygame.init()  # 遊戲初始化

screen = pygame.display.set_mode((width, height))  # 解析度(視窗大小 tuple)
clock = pygame.time.Clock()  # 對時間進行管理與操控

running = True

while running:
    clock.tick(FPS)  # 1秒鐘之內最多被執行10次(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新遊戲
    # 畫面顯示
    screen.fill(backgroundColor)  # RGB(tuple)
    pygame.display.update()


pygame.quit()
