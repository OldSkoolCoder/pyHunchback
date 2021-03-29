import pygame as pg 
import settings

class Platform(pg.sprite.Sprite):
    def __init__(self, x,y,w,h,imgTile):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image = imgTile
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



