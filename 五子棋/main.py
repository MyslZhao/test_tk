import pygame as pg
from random import choice
# -*- coding: utf-8 -*-
#相关数据与图片初始化
LOCA_ARGC=(554,532)
WHITE_PIC=pg.image.load(".\\whit.png")
BLACK_PIC=pg.image.load(".\\black.png")
BACKGROUND_PIC=pg.image.load(".\\background.jpg")
CHESSBOARD_PIC=pg.image.load(".\\chessboard.jpg")
ICO=pg.image.load(".\\icon.jpg")
COLOR={0:None,1:'白方',2:'黑方'}  # 定义颜色字典
COLOR_PIC={0:None,1:WHITE_PIC,2:BLACK_PIC}

class board:
    start_point=(20,20)
    pix_size = (0,0)
    size = (15, 15)
    x_loca=[]
    y_loca=[]
    bias = 5
    player = []  # 玩家列表，存储两个玩家对象
    def __init__(self, size: tuple[int, int], player1: 'player', player2: 'player'):
        self.pix_size = size  # 设置棋盘像素大小
        x_dist=int(self.pix_size[0] / (self.size[0]-1))
        y_dist=int(self.pix_size[0] / (self.size[0]-1))
        for i in range(14):
            self.x_loca.append(x_dist*i)
            self.y_loca.append(i*y_dist)
        self.player.append(player1)  # 添加玩家1
        self.player.append(player2)  # 添加玩家2
        return 0
    def check(self):
        pass
    def place_piece(self,player:'player',pix_loca:tuple[int,int]):
        for x in self.x_loca:
            for y in self.y_loca:
                m=(x-self.bias+self.start_point[0]-pix_loca[0])*(x+self.bias+self.start_point[0]-pix_loca[0])
                n=(y-self.bias+self.start_point[1]-pix_loca[1])*(y+self.bias+self.start_point[1]-pix_loca[1])
                if m < 0 and n < 0:
                    surface.blit(COLOR_PIC[player.color], (x+self.start_point[0] - 32, y+self.start_point[1] - 32))

    def start(self):
        turn=[False,False]
        turn[choice([0,1])]=True
        game=True
        while game:
            for i in range(1):
                if turn[i]:
                    self.place_piece(self.player[i],self.player[i].place_piece())
                    if self.check():
                        game=False
                    turn.reverse()
        self.result()

    def result(self):
        pass

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
        return str(self.score)
    def place_piece(self):
        loca=pg.mouse.get_pos()  # 获取鼠标位置
        return loca
        
def welcome_msg():
    #相关数据初始化
    label_color = (204,204,51)
    button_color = (255,255,255)
    label_text = "五子棋"
    button_text = "开始游戏"
    #相关对象初始化
    #ps:由于没有找到好的资源，暂时先用文本来代替
    #ps:之后肯定会来解决
    board=pg.Rect(175,167,300,300)
    button_obj = pg.font.SysFont('华文细黑',25).render(button_text, True, button_color)
    button_bg = pg.Rect(223,343, 200, 50)  # 创建按钮矩形
    label_obj = pg.font.SysFont('华文行楷', 75).render(label_text, True, label_color)
    pg.draw.rect(surface,(255,255,255),board)
    surface.blit(label_obj, (209,190))
    pg.draw.rect(surface, (204,204,0), button_bg)  #
    surface.blit(button_obj, (button_bg.x + 50, button_bg.y + 5))  # 绘制按钮文本
    pg.display.update()  # 更新显示
    start=False
    while not start:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                loca = pg.mouse.get_pos()
                x=(button_bg.x+button_bg.width-loca[0])*(button_bg.x-loca[0])
                y=(button_bg.y+button_bg.height-loca[1])*(button_bg.y-loca[1])
                if x < 0 and y < 0:
                    print("out")
                    surface.fill((0,0,0))
                    pg.display.flip()
                    start=True
    main()

            
def main():
    print("main start")
    disp(surface)
    white=player(1)
    black=player(2)
    game=board(LOCA_ARGC,white,black)
    game.start()

def disp(surface):
    surface.fill((255, 255, 255))  # 设置背景颜色为白色
    surface.blit(BACKGROUND_PIC, (0, 0))  # 绘制背景图(ps:找不到什么好图，只能先用围棋图代替)
    surface.blit(CHESSBOARD_PIC, (20, 20))  # 绘制棋盘
    pg.display.set_icon(ICO)  # 设置窗口图标
    pg.display.set_caption("五子棋")  # 设置窗口标题为"五子棋"
    pg.display.update()  # 更新显示



"""    
if self.color == 1:
            surface.blit(WHITE_PIC, (location[0] - 32, location[1] - 32))
        elif self.color == 2:
            surface.blit(BLACK_PIC, (location[0] - 32, location[1] - 32))
"""
pg.init() #pygame 初始化
pg.font.init()  # 初始化字体模块
surface = pg.display.set_mode((652, 652))
disp(surface)
welcome_msg() 

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print("退出游戏")
            done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())
