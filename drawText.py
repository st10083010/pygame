from typing import Text
import pygame

fontName = pygame.font.match_font('arial')
# pygame.font.match_font(字體名稱) 從電腦中尋找

textColor = (255, 255, 255)
currentHP_color = (0, 255, 0)


def draw_text(surf, text, size, x, y):
    # draw_text(寫在哪個平面上, 文字, 大小, X與Y座標)
    font = pygame.font.Font(fontName, size)  # (字體, 大小)
    textSurface = font.render(text, True, textColor)
    # 渲染文字(文字, 是否反鋸齒(anti-aliasing), 文字顏色)
    textRect = textSurface.get_rect()  # 定位文字
    textRect.centerx = x
    textRect.top = y
    surf.blit(textSurface, textRect)


def draw_health(surf, hp, x, y):
    # (平面，血量，座標)
    if hp <= 0:
        hp = 0
    # 檢查血量是否為負數，避免畫面奇怪()
    HP_BAR_HIGHT = 10
    HP_BAR_LENGTH = 100
    # 設定生命條的高度與寬度
    fill = (hp/100)*HP_BAR_LENGTH
    # 當前生命值
    outlineRect = pygame.Rect(x, y, HP_BAR_LENGTH, HP_BAR_HIGHT)
    # 白色外框
    fillRect = pygame.Rect(x, y, fill, HP_BAR_HIGHT)
    # 綠色矩形
    pygame.draw.rect(surf, currentHP_color, fillRect)
    pygame.draw.rect(surf, textColor, outlineRect, 2)
