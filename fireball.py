import pygame as pg 
import settings
vec = pg.math.Vector2

class FireBall(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game

        # Set animation modes
        self.direction= "Right"
        self.set = "1"

        # Load animation sets
        self.animationSets = {}
        self.animationSets['1'] = {}
        self.animationSets['1']['Right'] = self.LoadAnimationFrames('FireBall','1','Right')
        self.animationSets['1']['Left'] = self.LoadAnimationFrames('FireBall','1','Left')
        self.animationSets['2'] = {}
        self.animationSets['2']['Right'] = self.LoadAnimationFrames('FireBall','2','Right')
        self.animationSets['2']['Left'] = self.LoadAnimationFrames('FireBall','2','Left')
        self.animationSets['3'] = {}
        self.animationSets['3']['Right'] = self.LoadAnimationFrames('FireBall','3','Right')
        self.animationSets['3']['Left'] = self.LoadAnimationFrames('FireBall','3','Left')

        self.animatedFrameNo = 0
        self.image = self.animationSets["1"][self.direction][self.animatedFrameNo // 4]
        self.rect = self.image.get_rect()
        self.radius = 0

        self.position = vec(-100, 0)
        self.velocity = vec(0,0)
        self.active = False

    def update(self):
        self.image = self.animationSets[self.set][self.direction][self.animatedFrameNo // 4]
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.radius = int(self.rect.height * .9 / 2)
            
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
        if self.animatedFrameNo == 28:
            self.animatedFrameNo = 0

    def reactivateSprite(self,y,direction,speed,set):
        self.direction= direction
        self.set = set

        if self.direction == 'Left':
            speed = -speed

        if self.direction == "Right":
            x = - 100
        else:
            x = settings.STAGEWIDTH + 100

        self.position = vec(x, y)

        self.velocity = vec(speed,0)
        self.image = self.animationSets[self.set][self.direction][self.animatedFrameNo // 4]
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.height * .9 / 2)

        self.active = True

    def LoadAnimationFrames(self,asset,set,direction):
        animatedSet = []
        for frameNo in range(1,8):
            fileName = 'Assets/{0}/Effects_Fire_{1}_{2:02d}.png'.format(asset,set,frameNo)
            animatedImage = pg.image.load(fileName)#.convert()
            animatedImage = pg.transform.scale(animatedImage, (94,54))
            if direction == 'Left':
                animatedImage = pg.transform.flip(animatedImage, True, False)
            animatedImage.set_colorkey(settings.WHITE)
            animatedSet.append(animatedImage)
        return animatedSet
