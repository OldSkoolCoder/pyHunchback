import pygame as pg 
import random 
import game 

g = game.Game()
g.showStartScreen()
level = 1

g.new()

while g.running:
    g.showLevelStartScreen(level)
    g.nextChapter('{:02d}'.format(level))
    if g.bonusLife == True:
        g.bonusLife = False
        g.showBonusLife()

    if g.dead:
        if g.NoOfLives == 0:
            g.showGameOverScreen()
            g.running = False
    else:
        level += 1

pg.display.quit()
pg.quit()