import pygame as pg 
import settings
import game 
vec = pg.math.Vector2

class Ninja(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game

        # Set animation modes
        self.action= "Climb"
        self.direction= "Right"
        self.gliding = False

        # Load animation sets
        self.animationSets = {}
        self.animationSets['Idle'] = {}
        self.animationSets['Idle']['Right'] = self.LoadAnimationFrames('NinjaMan','Idle','Right')
        self.animationSets['Idle']['Left'] = self.LoadAnimationFrames('NinjaMan','Idle','Left')
        self.animationSets['Run'] = {}
        self.animationSets['Run']['Right'] = self.LoadAnimationFrames('NinjaMan','Run','Right')
        self.animationSets['Run']['Left'] = self.LoadAnimationFrames('NinjaMan','Run','Left')
        self.animationSets['Climb'] = {}
        self.animationSets['Climb']['Right'] = self.LoadAnimationFrames('NinjaMan','Climb','Right')
        self.animationSets['Climb']['Left'] = self.LoadAnimationFrames('NinjaMan','Climb','Left')
        self.animationSets['Glide'] = {}
        self.animationSets['Glide']['Right'] = self.LoadAnimationFrames('NinjaMan','Glide','Right')
        self.animationSets['Glide']['Left'] = self.LoadAnimationFrames('NinjaMan','Glide','Left')

        self.image = self.animationSets[self.action][self.direction][self.game.animatedFrameNo]
        self.rect = self.image.get_rect()
        self.radius = 0
        self.rect.center = (380, settings.SCREENHEIGHT - 10)
        self.position = vec(380, settings.SCREENHEIGHT - 10)

        self.FrameCounter = 0
        self.FPS = settings.FPS / 2

        self.velocity = vec(0,(-10/self.FPS))

    def update(self):
        self.rect.centerx = int(self.position.x)

        # wallHits = pg.sprite.spritecollide(self, self.game.walls, False)
        # if wallHits:
        #     for wall in wallHits:
        #         if wall.rect.top < self.rect.bottom:
        #             #wall.image.fill(settings.BLUE)
        #             self.acceleration.x = 0
        #             if self.velocity.x < 0:
        #                 self.rect.left = wall.rect.right
        #                 self.velocity.x = 0
        #             elif self.velocity.x > 0:
        #                 self.rect.right = wall.rect.left
        #                 self.velocity.x = 0

        #self.rect.centery = int(self.position.y)
        self.rect.bottom = int(self.position.y)

        platformHits = pg.sprite.spritecollide(self, self.game.walls, False)
        if not platformHits and not self.gliding:
            self.action = 'Glide'
            self.gliding = True
            self.position.y -= 50
            self.rect.bottom = int(self.position.y)
            self.velocity = vec((20/self.FPS),(4/self.FPS/2))


        elif platformHits and self.gliding:
            self.rect.bottom = platformHits[0].rect.top
            if self.position.x > self.game.player.position.x:
                self.velocity = ((-40 / self.FPS),0)
                self.action = "Run"
                self.direction= "Left"
            else:
                self.velocity = ((40 / self.FPS),0)
                self.action = "Run"
                self.direction= "Right"

        #self.position = self.rect.center

        self.image = self.animationSets[self.action][self.direction][self.game.animatedFrameNo]
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .9 / 2)
        self.rect.midbottom = self.position

        #if self.game.frameCounter == 0 or self.game.frameCounter == 30:
        #if self.gliding:
            #self.velocity = vec(1.4,0.05)
            #self.velocity = vec((5/60),(1/60))
        # Equation of Motion
        self.position += self.velocity #+ 0.5 * self.acceleration
        #else:
        #    self.position += vec(0,0) #+ 0.5 * self.acceleration


    def LoadAnimationFrames(self,asset,mode,direction):
        animatedSet = []
        for frameNo in range(0,10):
            fileName = 'Assets/{0}/{1}__{2:03d}.png'.format(asset,mode,frameNo)
            animatedImage = pg.image.load(fileName) #.convert()
            if mode == 'Glide':
                animatedImage = pg.transform.scale(animatedImage,(78,80))
            else:
                animatedImage = pg.transform.scale(animatedImage,(49,80))
            if direction == 'Left':
                animatedImage = pg.transform.flip(animatedImage, True, False)
            animatedImage.set_colorkey(settings.BLACK)
            animatedSet.append(animatedImage)
        return animatedSet
