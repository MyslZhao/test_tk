import pygame as pg
import threading as th
from time import sleep
# -*- coding: utf-8 -*-
#相关数据与图片初始化
LOCA_ARGC=(554,532)
WHITE_PIC=pg.image.load("五子棋\\whit.png")
BLACK_PIC=pg.image.load("五子棋\\black.png")
BACKGROUND_PIC=pg.image.load("五子棋\\background.jpg")
CHESSBOARD_PIC=pg.image.load("五子棋\\chessboard.jpg")
ICO=pg.image.load("五子棋\\icon.jpg")
COLOR={0:None,1:'白方',2:'黑方'}  # 定义颜色字典

class board:
    pix_size = (0,0)
    size = (15, 15)
    dist = (0,0)
    bias = 5
    player = [None:player, None:player]  # 玩家列表，存储两个玩家对象
    def __init__(self, size: tuple[int, int], player1: 'player', player2: 'player'):
        self.pix_size = size  # 设置棋盘像素大小
        self.dist = (int(self.pix_size[0] / self.size[0]), int(self.pix_size[0] / self.size[0]))
        self.player[1] = player1  # 设置玩家1
        self.player[2] = player2
        return 0
    def switch_turn(self):
        """切换玩家回合"""
        if self.player[1].if_turn():
            self.player[1].turn = False
            self.player[2].turn = True
        else:
            self.player[1].turn = True
            self.player[2].turn = False

class player:
    """玩家类"""
    score=0
    color=0
    turn = False
    def __init__(self, color:int):
        self.color = color
        self.score = 0
    def get_color(self):
        return COLOR[self.color]
    def get_score(self):
        return self.score
    def if_turn(self):
        return self.turn
    def place_piece(self,board):
        loca=pg.mouse.get_pos()  # 获取鼠标位置
        return loca
        
        





"""    
if self.color == 1:
            surface.blit(WHITE_PIC, (location[0] - 32, location[1] - 32))
        elif self.color == 2:
            surface.blit(BLACK_PIC, (location[0] - 32, location[1] - 32))
"""
pg.init() #pygame 初始化
pg.font.init()  # 初始化字体模块
surface = pg.display.set_mode((652, 652))
surface.fill((255, 255, 255))  # 设置背景颜色为白色
surface.blit(BACKGROUND_PIC, (0, 0))  # 绘制背景图(ps:找不到什么好图，只能先用围棋图代替)
surface.blit(CHESSBOARD_PIC, (20, 20))  # 绘制棋盘
pg.display.set_icon(ICO)  # 设置窗口图标
pg.display.set_caption("五子棋")  # 设置窗口标题为"五子棋"
pg.display.update()  # 更新显示

def welcome_msg():
    label_text = 'Hello, World!'
    label = pg.font.SysFont('Arial', 24).render(label_text, True, (0, 0, 255))
    surface.blit(label, (50, 50))
    
def main():
    pass
#pygame 循环


done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print("退出游戏")
            done = True
