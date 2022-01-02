from typing import Text
import pygame
import os


fontName = pygame.font.match_font('arial')
# pygame.font.match_font(字體名稱) 從電腦中尋找

for_CHT_text = os.path.join("font.ttf")

textColor = (255, 255, 255)  # for english
cht_text_color = (30, 144, 255)  # for zh_TW
currentHP_color = (0, 255, 0)  # health color
player_lives_icon_spacing = 30
# 玩家生命值圖片的間距


def draw_text(surf, text, size, x, y):
    # draw_text(寫在哪個平面上, 文字, 大小, X與Y座標)
    font = pygame.font.Font(fontName, size)  # (字體, 大小)
    textSurface = font.render(text, True, textColor)
    # 渲染文字(文字, 是否反鋸齒(anti-aliasing), 文字顏色)
    textRect = textSurface.get_rect()  # 定位文字
    textRect.centerx = x
    textRect.top = y
    surf.blit(textSurface, textRect)


def draw_text_forCHT(surf, text, size, x, y):
    # draw_text_forCHT(寫在哪個平面上, 文字, 大小, X與Y座標)
    font = pygame.font.Font(for_CHT_text, size)  # (字體, 大小)
    textSurface = font.render(text, True, cht_text_color)
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


def draw_lives(surf, lives, img, x, y):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + player_lives_icon_spacing*i
        # 設定圖片與圖片的間距，避免重疊
        img_rect.y = y
        surf.blit(img, img_rect)
