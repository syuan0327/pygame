import pygame,random

#            R    G     B
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
RED1=(100,0,0)
PINK=(255,240,240)
BLUE=(200,200,255)

    
#初始化遊戲
pygame.init()


#設定視窗大小size(橫,直)
size = (700, 500)
#創建視窗
screen = pygame.display.set_mode(size)
#設定視窗名稱
pygame.display.set_caption("第一個遊戲")
#設定開關
done = False

#控制畫面速度
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #事件偵測list
    
               
   
    
    screen.fill(BLACK)
    #放主要程式碼的地方!!!!
    
    #更新畫面
    pygame.display.flip()
    #每秒更新60次
    clock.tick(60)
#關掉pygame
pygame.quit()

