import pygame as pg 
import settings
vec = pg.math.Vector2

class Coin(pg.sprite.Sprite):
    def __init__(self,game,x,y,size):
        pg.sprite.Sprite.__init__(self)
        self.game = game

        # Set animation modes

        # Load animation sets
        self.animationSets = []
        self.animationSets = self.LoadAnimationFrames('RotatingCoins','tile',size)

        self.animatedFrameNo = 0
        self.image = self.animationSets[self.animatedFrameNo // 4]
        self.rect = self.image.get_rect()

        self.position = vec(x, y)

    def update(self):
        self.image = self.animationSets[self.animatedFrameNo // 3]
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .9 / 2)

        self.rect.center = self.position

        self.animatedFrameNo +=1
        if self.animatedFrameNo == 63:
            self.animatedFrameNo = 0

    def LoadAnimationFrames(self,asset,mode,size):
        animatedSet = []
        for frameNo in range(0,21):
            fileName = 'Assets/{0}/{1}{2:03d}.png'.format(asset,mode,frameNo)
            animatedImage = pg.image.load(fileName) #.convert()
            animatedImage = pg.transform.scale(animatedImage, (size,size))
            #animatedImage.set_colorkey(settings.BLACK)
            animatedSet.append(animatedImage)
        return animatedSet
