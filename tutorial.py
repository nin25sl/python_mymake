import pygame as pg
import sys, time

pg.init()
GAMEN = pg.display.set_mode((400, 300))
pg.display.set_caption('Hello World!')
pg.draw.rect(GAMEN, (255, 0, 0), (150, 50, 100, 50))

x = 50
dx = 10
while True:
    GAMEN.fill((0, 120, 120))
    pg.draw.rect(GAMEN, (255, 120, 120), (x, 150, 100, 50))
    pg.display.update()

    if x >= 300 or x <= 0:
        dx = -dx
    x += dx
    time.sleep(0.05)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()