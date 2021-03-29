import pygame as pg 
import settings
vec = pg.math.Vector2

class Rock(pg.sprite.Sprite):
    def __init__(self,game,size):
        pg.sprite.Sprite.__init__(self)
        self.game = game

        # Set animation modes
        self.direction= "Right"

        # Load animation sets
        self.animationSets = {}
        self.animationSets['Right'] = self.LoadAnimationFrames('Rocks','tile','Right',size)
        self.animationSets['Left'] = self.LoadAnimationFrames('Rocks','tile','Left',size)

        self.animatedFrameNo = 0
        self.image = self.animationSets[self.direction][self.animatedFrameNo // 4]
        self.rect = self.image.get_rect()
        self.radius = 0

        self.position = vec(-100, 0)
        self.velocity = vec(0,0)
        self.size = size
        self.active = False

    def update(self):
        self.image = self.animationSets[self.direction][self.animatedFrameNo // 4]
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .9 / 2)

        self.rect.center = self.position

        if self.active:            
            self.position += self.velocity

            if self.position.x < -150:
                #self.position.x = settings.STAGEWIDTH + 50 
                self.active = False
                self.velocity.x = 0
                #self.kill()

            if self.position.x > settings.STAGEWIDTH + 150:
                #self.position.x = -50
                self.active = False
                self.velocity.x = 0
                #self.kill()

        self.animatedFrameNo +=1
        if self.animatedFrameNo == 128:
            self.animatedFrameNo = 0

    def reactivateSprite(self,y,direction,speed):
        self.direction= direction

        if self.direction == 'Left':
            speed = -speed

        if self.direction == "Right":
            x = - 100
        else:
            x = settings.STAGEWIDTH + 100

        self.position = vec(x, y)

        self.velocity = vec(speed,0)

        self.image = self.animationSets[self.direction][self.animatedFrameNo // 4]
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .9 / 2)
        self.rect.center = self.position
        self.active = True

    def LoadAnimationFrames(self,asset,mode,direction,size):
        animatedSet = []
        for frameNo in range(0,32):
            fileName = 'Assets/{0}/{1}{2:03d}.png'.format(asset,mode,frameNo)
            animatedImage = pg.image.load(fileName).convert()
            animatedImage = pg.transform.scale(animatedImage, (size,size))
            if direction == 'Right':
                animatedImage = pg.transform.flip(animatedImage, True, False)
            animatedImage.set_colorkey(settings.BLACK)
            animatedSet.append(animatedImage)
        return animatedSet
