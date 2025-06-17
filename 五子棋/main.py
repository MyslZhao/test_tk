import pygame as pg
# -*- coding: utf-8 -*-
bit_loca=(554,532)

pg.init() #pygame 初始化
surface = pg.display.set_mode((652, 652))
pg.display.set_caption("五子棋")  # 设置窗口标题为"五子棋"
surface.fill((255, 255, 255))  # 设置背景颜色为白色

pg.display.set_icon(pg.image.load("五子棋\\icon.jpg"))  # 设置窗口图标

surface.blit(pg.image.load("五子棋\\background.jpg"), (0, 0))  # 绘制背景图(ps:找不到什么好图，只能先用围棋图代替)
surface.blit(pg.image.load("五子棋\\chessboard.jpg"), (20, 20))  # 绘制棋盘
pg.display.update()  # 更新显示




#pygame 循环
done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True