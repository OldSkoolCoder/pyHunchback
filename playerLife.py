import pygame as pg 
import settings
import game, player
vec = pg.math.Vector2

class PlayerLife(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        pg.sprite.Sprite.__init__(self)
        self.game = game

        # Set animation modes
        self.action= "Idle"
        self.direction= "Right"

        # Load animation sets
        self.animationSets = {}
        self.animationSets['Idle'] = {}
        self.animationSets['Idle']['Right'] = self.loadAnimationFrames('Knight','Idle','Right')

        self.image = self.animationSets[self.action][self.direction][0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.position = vec(x, y)
        self.x = x
        self.y = y

        self.frameCounter = 0

    def update(self):
        self.frameCounter += 1
        if self.frameCounter >= 40:
                self.frameCounter = 0
        self.getNextAnimation()

        self.rect.centerx = -(self.game.scroll.x) + self.x
        self.position.x = -(self.game.scroll.x) + self.x

        #self.rect.centerx = (self.game.player.position.x - (settings.SCREENWIDTH / 2) + self.x)
        #self.position.x = (self.game.player.position.x - (settings.SCREENWIDTH / 2) + self.x)

    def loadAnimationFrames(self,asset,mode,direction):
        animatedSet = []
        for frameNo in range(1,11):
            fileName = 'Assets/{0}/{1} ({2}).png'.format(asset,mode,frameNo)
            animatedImage = pg.image.load(fileName)#.convert()
            animatedImage = pg.transform.scale(animatedImage, (33,40))
            if direction == 'Left':
                animatedImage = pg.transform.flip(animatedImage, True, False)
            #tileImage.set_colorkey(settings.WHITE)
            animatedSet.append(animatedImage)
        return animatedSet

    def getNextAnimation(self):
        animatedFrameNo = int(self.frameCounter // 4)
        self.image = self.animationSets[self.action][self.direction][animatedFrameNo]
        self.rect = self.image.get_rect()
        self.rect.center = self.position
