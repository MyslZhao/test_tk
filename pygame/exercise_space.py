import pygame as pg
# -*- coding: utf-8 -*-
# Pygame练习空间

# 初始化Pygame
pg.init()
# 设置窗口大小
size = (700, 500)
screen = pg.display.set_mode(size)

# 设置窗口标题
pg.display.set_caption("abcde")

# 设置矩形位置和大小
rect_x = 50
rect_y = 50
rect_width = 50
rect_height = 50

# 设置颜色
red = (255, 0, 0)

# 游戏循环
done = False

screen.fill((255, 255, 255))
pg.display.update()
while not done:
    # 处理事件
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    # 填充窗口颜色
    

    # 绘制矩形
    pg.draw.rect(screen, red, [rect_x, rect_y, rect_width, rect_height])

    # 更新窗口
    pg.display.update()

# 退出Pygame 

