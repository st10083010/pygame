from typing import Text
import pygame

fontName = pygame.font.match_font('arial')
# pygame.font.match_font(字體名稱) 從電腦中尋找

textColor = (255, 255, 255)


def draw_text(surf, text, size, x, y):
    # draw_text(寫在哪個平面上, 文字, 大小, X與Y座標)
    font = pygame.font.Font(fontName, size)  # (字體, 大小)
    textSurface = font.render(text, True, textColor)
    # 渲染文字(文字, 是否反鋸齒(anti-aliasing), 文字顏色)
    textRect = textSurface.get_rect()  # 定位文字
    textRect.centerx = x
    textRect.top = y
    surf.blit(textSurface, textRect)
