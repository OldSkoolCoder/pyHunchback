import pygame as pg
import random 
import settings

class Enemies:
    def __init__(self,type,delaySec,freqSecs,height,direction,speed,size,set):
        self.type = type
        self.delaySec = delaySec
        self.freqSecs = freqSecs
        self.height = height
        self.direction = direction
        self.speed = speed
        self.size = size
        self.set = set

        self.frameCounter = 0
        self.secondCounter = 0
        self.secondsRemaining = delaySec

        self.newSpriteNeeded = False

    def update(self):
        self.frameCounter +=1
        if self.frameCounter == settings.FPS:
            self.frameCounter = 0
            self.secondCounter +=1
            self.secondsRemaining -=1
            if self.secondsRemaining == 0:
                self.secondsRemaining = self.freqSecs
                self.newSpriteNeeded = True


