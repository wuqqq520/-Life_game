#coding=utf-8
import pygame
import sys
import time
import lifegame
import numpy as np
########################################################################
class screen():

    def __init__(self,size_x,size_y):
        self.width=1
        self.Cells_shape='rect'
        pygame.init()  # 初始化pygame
        if self.Cells_shape=='rect':
            size = width, height = size_x*(self.width+1)+40, size_y*(self.width+1)+40  # 设置窗口大小
        else:
            size = width, height = size_x*(2*self.width+1)+40, size_y*(2*self.width+1)+40
        self.background = pygame.display.set_mode(size)  # 显示窗口
        color = (0, 0, 0)  # 设置颜色   
        clock = pygame.time.Clock() 
        self.life=lifegame.initial(size_x, size_y)  
        lf=np.where(self.life>0)
        self.undatascreen(lf)        
        time.sleep(5)
        while True:  # 死循环确保窗口一直显示
            clock.tick(30)
            for event in pygame.event.get():  # 遍历所有事件
                if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                    sys.exit()  

            lfdata=lifegame.iteration(self.life)
            lf=np.where(lfdata>0)
            self.undatascreen(lf)
            self.life=lfdata
            #time.sleep(1)            

                    
    def undatascreen(self,lfdata):
        color = (0, 0, 0)
        self.background.fill(color) 
        if self.Cells_shape=='rect':
            for sz in range(len(lfdata[0])):
                pygame.draw.rect(self.background,(188,188,188),((lfdata[0][sz]*(self.width+1)+20, lfdata[1][sz]*(self.width+1)+20), (self.width, self.width)))
        else:
            for sz in range(len(lfdata[0])):
                pygame.draw.circle(self.background, (188, 188, 188), (lfdata[0][sz]*(2*self.width+1)+20, lfdata[1][sz]*(2*self.width+1)+20), self.width)
        pygame.display.flip()  # 更新全部显示    
        
    def qut():
        pygame.quit()  # 退出pygame


a=screen(1000,800)
a.undatascreen()
a.qut()




