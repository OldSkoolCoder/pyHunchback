import pygame as pg 
import settings
vec = pg.math.Vector2

class NinjaGirl(pg.sprite.Sprite):
    def __init__(self,game, wallPlacement, delaySec, freqSecs, direction):
        pg.sprite.Sprite.__init__(self)
        self.game = game

        # Set animation modes
        self.action= "Idle"
        self.direction= "Right"
        self.wallPlacement = wallPlacement
        self.delaySec = delaySec
        self.freqSecs = freqSecs

        # Load animation sets
        self.animationSets = {}
        self.animationSets['Idle'] = {}
        self.animationSets['Idle']['Right'] = self.loadAnimationFrames('NinjaGirl','Idle','Right')
        self.animationSets['Idle']['Left'] = self.loadAnimationFrames('NinjaGirl','Idle','Left')
        self.animationSets['Jump'] = {}
        self.animationSets['Jump']['Right'] = self.loadAnimationFrames('NinjaGirl','Jump','Right')
        self.animationSets['Jump']['Left'] = self.loadAnimationFrames('NinjaGirl','Jump','Left')

        self.image = self.animationSets[self.action][self.direction][0]
        self.rect = self.image.get_rect()
        self.radius = 0
        self.rect.center = (wallPlacement, 220)
        self.position = vec(wallPlacement, 220)

        self.velocity = vec(0,0)
        self.acceleration = vec(0,0)
        self.frameCounter = 0
        self.animatedFrameNo = 0
        self.secondCounter = 0
        self.secondsRemaining = delaySec
        self.jumping = False

    def update(self):
        self.rect.centerx = int(self.position.x)

        self.performRun()

        if self.game.player.position.x <= self.position.x :
            self.direction = "Left"
        else:
            self.direction = "Right"

        self.frameCounter +=1
        if self.frameCounter == settings.FPS:
            self.frameCounter = 0
            self.secondCounter +=1
            self.secondsRemaining -=1
            if self.secondsRemaining == 0:
                self.secondsRemaining = self.freqSecs
                self.jump()

    def jump(self):
        if not self.jumping:
            # Check if we are standing on a platform, if so.... Jump
            self.rect.y += 5
            platformHits = pg.sprite.spritecollide(self, self.game.walls, False)
            self.rect.y -= 5
            if platformHits:
                if self.rect.bottom >= platformHits[0].rect.top:
                    self.velocity.y = -settings.JUMP_HEIGHT
                    self.jumping = True
                    self.action = "Jump"
                    self.game.frameCounter = 0
                    #platformHits[0].image.fill(settings.GREEN)

    def loadAnimationFrames(self,asset,mode,direction):
        animatedSet = []
        for frameNo in range(0,10):
            fileName = 'Assets/{0}/{1}__{2:03d}.png'.format(asset,mode,frameNo)
            animatedImage = pg.image.load(fileName)#.convert()
            if mode == 'Glide':
                animatedImage = pg.transform.scale(animatedImage,(78,80))
            elif mode == 'Jump':
                animatedImage = pg.transform.scale(animatedImage,(59,80))
            else:
                animatedImage = pg.transform.scale(animatedImage,(49,80))
            if direction == 'Left':
                animatedImage = pg.transform.flip(animatedImage, True, False)
            #tileImage.set_colorkey(settings.WHITE)
            animatedSet.append(animatedImage)
        return animatedSet

    def performRun(self):
        wallHits = pg.sprite.spritecollide(self, self.game.walls, False)
        if wallHits:
            for wall in wallHits:
                if wall.rect.top < self.rect.bottom:
                    #wall.image.fill(settings.BLUE)
                    self.acceleration.x = 0
                    if self.velocity.x < 0:
                        self.rect.left = wall.rect.right
                        self.velocity.x = 0
                    elif self.velocity.x > 0:
                        self.rect.right = wall.rect.left
                        self.velocity.x = 0

        self.gravityCheck()
        self.getNextAnimation()
        self.acceleration = vec(0, settings.GRAVITY)

        if not self.jumping:
            self.action = "Idle"
            
        self.calculateNewPosition()

    def getNextAnimation(self):
        self.image = self.animationSets[self.action][self.direction][self.game.animatedFrameNo]
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.center = self.position
        #self.rect.inflate_ip(-30,-30)

    def performDying(self):
        self.gravityCheck()
        self.getNextAnimation()
        self.calculateNewPosition()

    def calculateNewPosition(self):
        # Apply Friction
        self.velocity.x += self.velocity.x * settings.PLAYER_FRICTION

        if abs(self.velocity.x) < 0.1:
            self.velocity.x = 0

        # Equation of Motion
        self.velocity += self.acceleration
        self.position += self.velocity #+ 0.5 * self.acceleration

    def gravityCheck(self):
        self.rect.centery = int(self.position.y)

        if self.velocity.y > 0:
            platformHits = pg.sprite.spritecollide(self, self.game.walls, False)
            if platformHits:
                if self.rect.bottom < (platformHits[0].rect.top + (self.velocity.y * 1.1)):
                    #platformHits[0].image.fill(settings.RED)
                    self.rect.bottom = platformHits[0].rect.top
                    self.velocity.y = 0
                    self.jumping = False

        self.position = self.rect.center

    def enemyHit(self):
        enemyHits = pg.sprite.spritecollide(self, self.game.enemies, False, pg.sprite.collide_circle) 
        if enemyHits:
            self.game.status = settings.STATUS_DYING
            self.action = "Dead"
            self.velocity = vec(0,0)
            self.frameCounter = 0
            

