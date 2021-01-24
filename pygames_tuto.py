import pygame
from pygame.locals import *
import sys
import random

def setScreen():
    pygame.init()
    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption("Test")

    return screen

def setColors(color):
    black = (  0,   0,   0)
    white = (255, 255, 255)
    red   = (255,   0,   0)
    green = (  0, 255,   0)
    blue  = (  0,   0, 255)

    return color

def setOutside(screen):
    size = (30,30)
    column = outsideConfig()
    rectConfig = pygame.Surface(size)
    x = 120
    y = 140
    for i in range(22):
        ytemp = y + i * rectConfig.get_height()
        for j in range(12):
            if column[i][j] == 1:
                xtemp = x + j * rectConfig.get_width()
                pygame.draw.rect(screen, setColors('red'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2),2)
                pygame.draw.rect(screen, setColors('white'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2))

def outsideConfig():
    # width = 12, height = 22
    column = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

    column[0]  = [1,1,1,1,0,0,0,0,1,1,1,1]
    column[1]  = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[2]  = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[3]  = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[4]  = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[5]  = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[6]  = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[7]  = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[8]  = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[9]  = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[10] = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[11] = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[12] = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[13] = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[14] = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[15] = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[16] = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[17] = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[18] = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[19] = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[20] = [1,0,0,0,0,0,0,0,0,0,0,1]
    column[21] = [1,1,1,1,1,1,1,1,1,1,1,1]

    return column

def tetraminoConfig(minoparams,column):   
    if minoparams == 2:#J
        column[0][6] = 2
        column[1][6] = 2
        column[2][5] = 2
        column[2][6] = 2
    elif minoparams == 3:#L
        column[0][5] = 3
        column[1][5] = 3
        column[2][5] = 3
        column[2][6] = 3
    elif minoparams == 4:#T
        column[0][5] = 4
        column[1][4] = 4
        column[1][5] = 4
        column[1][6] = 4
    elif minoparams == 5:#Z
        column[0][4] = 5
        column[0][5] = 5
        column[1][5] = 5
        column[1][6] = 5
    elif minoparams == 6:#S
        column[0][5] = 6
        column[0][6] = 6
        column[1][4] = 6
        column[1][5] = 6
    elif minoparams == 7:#O
        column[0][5] = 7
        column[0][6] = 7
        column[1][5] = 7
        column[1][6] = 7
    elif minoparams == 8:#I
        column[0][5] = 8
        column[1][5] = 8
        column[2][5] = 8
        column[3][5] = 8
    
    return column

def setTetramino(column,screen, minoparams):
    screen.fill(setColors('black'))
    setColumn = tetraminoConfig(minoparams,column)
    return setColumn

def drawTetramino(column, screen):
    size = (30,30)
    rectConfig = pygame.Surface(size)
    screen.fill(setColors('black'))
    x = 120
    y = 140
    for i in range(22):
        ytemp = y + i * rectConfig.get_height()
        for j in range(12):
            if column[i][j] == 1:
                xtemp = x + j * rectConfig.get_width()
                pygame.draw.rect(screen, setColors('red'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2),2)
                pygame.draw.rect(screen, setColors('white'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2))
            elif column[i][j] == 2:
                xtemp = x + j * rectConfig.get_width()
                pygame.draw.rect(screen, setColors('red'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2),2)
                pygame.draw.rect(screen, setColors('blue'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2))
            elif column[i][j] == 3:
                xtemp = x + j * rectConfig.get_width()
                pygame.draw.rect(screen, setColors('red'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2),2)
                pygame.draw.rect(screen, 'orange', Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2))
            elif column[i][j] == 4:
                xtemp = x + j * rectConfig.get_width()
                pygame.draw.rect(screen, setColors('red'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2),2)
                pygame.draw.rect(screen, 'purple', Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2))
            elif column[i][j] == 5:
                xtemp = x + j * rectConfig.get_width()
                pygame.draw.rect(screen, setColors('red'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2),2)
                pygame.draw.rect(screen, setColors('red'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2))
            elif column[i][j] == 6:
                xtemp = x + j * rectConfig.get_width()
                pygame.draw.rect(screen, setColors('red'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2),2)
                pygame.draw.rect(screen, 'green', Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2))
            elif column[i][j] == 7:
                xtemp = x + j * rectConfig.get_width()
                pygame.draw.rect(screen, setColors('red'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2),2)
                pygame.draw.rect(screen, 'yellow', Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2))
            elif column[i][j] == 8:
                xtemp = x + j * rectConfig.get_width()
                pygame.draw.rect(screen, setColors('red'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2),2)
                pygame.draw.rect(screen, 'skyblue', Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2))

def downMove(column,screen, minoparams):
    for i in range(21,-1,-1):
        for j in range(11,-1,-1):
            if column[i][j] > 1:
                column[i+1][j] = minoparams
                column[i][j] = 0
                        

    drawTetramino(column, screen)

def main():
    minos = [2, 3, 4, 5, 6, 7, 8]
    screen = setScreen()
    setOutside(screen)
    FPS = 30
    fpsClock = pygame.time.Clock()
    
    while(1):
        minoparams = random.choice(minos)
        #後削除予定
        column = outsideConfig()
        column = setTetramino(column,screen,minoparams)
        drawTetramino(column, screen)
        i = 0
        while i < 10:
            downMove(column, screen, minoparams)
            pygame.time.delay(1000)
            pygame.display.update()
            i += 1
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.time.delay(1000)
        pygame.display.update()
        fpsClock.tick(FPS)
        if len(minos) == 1:
            minos = [2, 3, 4, 5, 6, 7, 8]
        else:
            minos.remove(minoparams)

if __name__ == "__main__":
    main()


