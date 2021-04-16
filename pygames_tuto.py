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
    # width = 12, height = 22 column[i][j]=> x = j y = i
    column = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

    column[0]  = [1,0,0,0,0,0,0,0,0,0,0,1]
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
            elif column[i][j] == 9:
                xtemp = x + j * rectConfig.get_width()
                pygame.draw.rect(screen, setColors('red'), Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2),2)
                pygame.draw.rect(screen, 'pink', Rect(xtemp,ytemp,rectConfig.get_width()-2,rectConfig.get_height()-2))

def downMove(column,screen, minoparams):
    getrollColumn = getColumnTetramino(column, minoparams)
    temp = 0
    comp = 21
    for i in range(4):
        #print([i])
        #print(getrollColumn[i][1])
        if getrollColumn[i][1] + 1 == 21:
            temp = 1
        elif column[getrollColumn[i][1] + 1][getrollColumn[i][0]] == 9:
            temp = 1
        else:
            pass
    for i in range(3,-1,-1):
        if temp == 1:
            column[getrollColumn[i][1]][getrollColumn[i][0]] = 9
        else:
            column[getrollColumn[i][1] + 1][getrollColumn[i][0]] = minoparams

    drawTetramino(column, screen)

    if temp == 1:
        return False
    else:
        return True

def getColumnTetramino(column, minoparams):
    tetraminoX = 0
    tetraminoY = 0
    getrollColumn = [0,1,2,3]
    tetraminoMax = 0
    for i in range(22):
        for j in range(12):
            if column[i][j] == minoparams:
                tetraminoX = j
                tetraminoY = i
                getrollColumn[tetraminoMax] = [tetraminoX, tetraminoY]
                #print(tetraminoX, tetraminoY, getrollColumn)
                column[i][j] = 0
                tetraminoMax += 1
    #print(getrollColumn)
    return getrollColumn

def rightRolling(column, screen, minoparams):
    #columnをとってくる。３番目に合わせて全てを原点に移動、x = y y = x(y軸が今回は反対)を行い、並行移動した分を元に戻す。
    tetraminoX = 0
    tetraminoY = 0
    getrollColumn = [0,1,2,3]
    tetraminoMax = 0
    for i in range(22):
        for j in range(12):
            if column[i][j] == minoparams:
                tetraminoX = j
                tetraminoY = i
                getrollColumn[tetraminoMax] = [tetraminoX, tetraminoY]
                column[i][j] = 0
                tetraminoMax += 1

    tetraminoX = getrollColumn[2][0]
    tetraminoY = getrollColumn[2][1]
    for i in range(4):
        print([getrollColumn[i]])

    for i in range(4):
        for j in range(2):
            if j == 0:
                getrollColumn[i][j] -= tetraminoX
            else:
                getrollColumn[i][j] -= tetraminoY

    print(tetraminoX, tetraminoY)
    for i in range(4):
        temp = -getrollColumn[i][0]
        getrollColumn[i][0] = -getrollColumn[i][1]
        getrollColumn[i][1] = temp
        print([getrollColumn[i][0],getrollColumn[i][1]])

    print("")
    for i in range(4):
        for j in range(2):
            if j == 0:
                getrollColumn[i][j] += tetraminoX
            else:
                getrollColumn[i][j] += tetraminoY

    for i in range(4):
        print(getrollColumn[i])
    print("")

    for i in range(4):
        column[getrollColumn[i][1]][getrollColumn[i][0]] = minoparams
    #drawTetramino(column,screen)
    return column

def parallelMoving(column, screen, minoparams, moveparam):
    getrollColumn = getColumnTetramino(column, minoparams)
    temp = 0
    #print(getrollColumn)
    for i in range(4):
        if getrollColumn[i][0] + moveparam == 0:
            temp = 1
        elif getrollColumn[i][0] + moveparam == 11:
            temp = 1
        elif column[getrollColumn[i][1]][getrollColumn[i][0] + moveparam] == 9:
            temp = 1
        else:
            pass

    for i in range(4):
        if temp == 0:
            column[getrollColumn[i][1]][getrollColumn[i][0] + moveparam] = minoparams
        else:
            column[getrollColumn[i][1]][getrollColumn[i][0]] = minoparams
    #drawTetramino(column, screen)
    return column

def Rolling(column, minoparams, screen):
    #getrollColumn = getColumnTetramino(column, minoparams)
    tetraminoX = 0
    tetraminoY = 0
    getrollColumn = [0,1,2,3]
    getganponColumn = [0,1,2,3]
    tetraminoMax = 0
    for i in range(22):
        for j in range(12):
            if column[i][j] == minoparams:
                tetraminoX = j
                tetraminoY = i
                getrollColumn[tetraminoMax] = [tetraminoX, tetraminoY]
                #print(tetraminoX, tetraminoY, getrollColumn)
                getganponColumn[tetraminoMax] = [i,j]
                column[i][j] = 0
                tetraminoMax += 1
    sortGetColumn = sorted(getrollColumn)

    temp = 0
    if minoparams == 8:
        if sortGetColumn[0][0] == sortGetColumn[1][0]:
            temp = 1
        else:
            pass
        #回転col
        prepCol = [[0 for j in range(4)]for i in range(4)]
        #左上のcolの用意
        tempCol = []
        for i in range(4):
            for j in range(4):
                if temp == 1:
                    tempCol = [sortGetColumn[0][1], sortGetColumn[0][0] - 1]
                    if i == 1:
                        prepCol[i][j] = 1
                    else:
                        prepCol[i][j] = 0
                else:
                    tempCol = [sortGetColumn[0][1]-1, sortGetColumn[0][0]]
                    if j == 1:
                        prepCol[i][j] = 1
                    else:
                        prepCol[i][j] = 0

        newPrepCol = [[0 for j in range(4)]for i in range(4)]
        temp = 0
        for i in range(4):
            for j in range(4):
                newPrepCol[i][j] = prepCol[i][3-j]
                if newPrepCol[i][j] == 1:
                    if tempCol[1] + j < 11 and tempCol[1] + j > 0:
                        pass
                    else:
                        temp = 1

        if temp == 1:
            for i in range(4):
                column[getganponColumn[i][0]][getganponColumn[i][1]] = minoparams
        else:
            for i in range(4):
                for j in range(4):
                    if newPrepCol[i][j] == 1:
                        print(newPrepCol)
                        column[tempCol[0] + i][tempCol[1] + j] = minoparams
        #drawTetramino(column, screen)
        return column

    else:
        prepCol = [[0 for j in range(4)]for i in range(4)]
        tempCol = []
        tempX = []
        tempY = []
        for i in range(4):
            tempX.append(sortGetColumn[i][0])
            tempY.append(sortGetColumn[i][1])

        #iはx軸、jはy軸
        x = 0
        for i in range(4):
            if x == 4:
                break;
            for j in range(4):
                tempCol = [min(tempX) - 1, min(tempY) - 1]
                #print(tempCol)
                #print([i,sortGetColumn[x][0] - tempCol[0]], [j,sortGetColumn[x][1] - tempCol[1]] )
                if i == sortGetColumn[x][0] - tempCol[0] and j == sortGetColumn[x][1] - tempCol[1]:
                    prepCol[i][j] = 1
                    x += 1
                    if x == 4:
                        break;
                else:
                    pass

        temp = 0
        newPrepCol = [[0 for j in range(4)]for i in range(4)]
        for i in range(4):
            for j in range(4):
                newPrepCol[i][j] = prepCol[i][3-j]
                if newPrepCol[i][j] == 1:
                    if tempCol[0] + j < 11 and tempCol[0] + j > 0:
                        pass
                    else:
                        temp = 1

        if temp == 1:
            for i in range(4):
                column[getganponColumn[i][0]][getganponColumn[i][1]] = minoparams
        else:
            for i in range(4):
                for j in range(4):
                    if newPrepCol[i][j] == 1:
                        column[tempCol[1] + i][tempCol[0] + j] = minoparams
        #drawTetramino(column, screen)
        return column

def finishTetris(column):
    if column[0][4] == 9 or column[0][5] == 9 or column[0][6] == 9:
        return False
    return True

def deleteColumns(column):
    temp = []
    for i in range(21):
        if 0 in column[i]:
            pass
        else:
            temp.append(i)
       
    for i in temp:
        for j in range(i, -1, -1):
            print(j)
            if j == 0:
                column[j] = [1,0,0,0,0,0,0,0,0,0,0,1]
            else:
                column[j] = column[j-1]
    return column

def main():
    minos = [2, 3, 4, 5, 6, 7, 8]
    screen = setScreen()
    setOutside(screen)
    FPS = 30
    fpsClock = pygame.time.Clock()
    column = outsideConfig()
    #font1 = pygame.font.SysFont(None, 50)
    #finishText = font1.render("Finish", True, (0,0,0))

    while True:
        minoparams = random.choice(minos)
        column = setTetramino(column,screen,minoparams)
        drawTetramino(column, screen)
        temp = 0
        pygame.time.delay(150)
        while True:
            temp = 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        column = parallelMoving(column, screen, minoparams, 1)
                    elif event.key == K_LEFT:
                        column = parallelMoving(column, screen, minoparams, -1)
                    elif event.key == K_UP:
                        column = Rolling(column, minoparams, screen)
                    drawTetramino(column, screen)
                    temp = 1

            if temp == 0:
                if downMove(column, screen, minoparams) is False:
                    column = deleteColumns(column)
                    drawTetramino(column, screen)
                    if finishTetris(column) is False:
                        temp = 2
                    break

            # if finishTetris(column) is False:
            #     temp = 2
            #     print(temp)
            #     break;

            pygame.time.delay(150)
            pygame.display.update()

        if temp == 2:
            break
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            fpsClock.tick(FPS)
            if len(minos) == 1:
                minos = [2, 3, 4, 5, 6, 7, 8]
            else:
                minos.remove(minoparams)
    pygame.display.update()
    pygame.time.delay(5000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


