import pygame as pg 
import settings
vec = pg.math.Vector2

class Axe(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game

        # Set animation modes
        self.direction= "Right"
        self.colour = "Blue"

        # Load animation sets
        self.animationSets = {}
        self.animationSets['Blue'] = {}
        self.animationSets['Blue']['Right'] = self.LoadAnimationFrames('Axe','Blue','Right')
        self.animationSets['Blue']['Left'] = self.LoadAnimationFrames('Axe','Blue','Left')
        self.animationSets['Red'] = {}
        self.animationSets['Red']['Right'] = self.LoadAnimationFrames('Axe','Red','Right')
        self.animationSets['Red']['Left'] = self.LoadAnimationFrames('Axe','Red','Left')

        self.animatedFrameNo = 0
        self.image = self.animationSets[self.colour][self.direction][self.animatedFrameNo // 4]
        self.rect = self.image.get_rect()
        self.radius = 0

        self.position = vec(-100, 0)
        self.velocity = vec(0,0)
        self.active = False

    def update(self):
        self.image = self.animationSets[self.colour][self.direction][self.animatedFrameNo // 2]
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.radius = 35

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
        if self.animatedFrameNo == 64:
            self.animatedFrameNo = 0

    def reactivateSprite(self,y,direction,speed, colour):
        self.direction= direction
        self.colour = colour

        if self.direction == 'Left':
            speed = -speed

        if self.direction == "Right":
            x = - 100
        else:
            x = settings.STAGEWIDTH + 100

        self.position = vec(x, y)

        self.image = self.animationSets[self.colour][self.direction][self.animatedFrameNo // 2]
        self.rect = self.image.get_rect()
        self.radius = 35

        self.velocity = vec(speed,0)
        self.active = True

    def LoadAnimationFrames(self,asset,colour,direction):
        animatedSet = []
        for frameNo in range(0,32):
            fileName = 'Assets/{0}/{1}AxeSmall.png'.format(asset,colour)
            animatedImage = pg.image.load(fileName).convert()
            #animatedImage = pg.transform.scale(animatedImage, (size,size))
            animatedImage = pg.transform.rotate(animatedImage, 11.25*frameNo)
            if direction == 'Right':
                animatedImage = pg.transform.flip(animatedImage, True, False)
            animatedImage.set_colorkey(settings.BLACK)
            animatedSet.append(animatedImage)
        return animatedSet
