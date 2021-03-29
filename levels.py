import pygame as pg
import random
import json
import settings
import enemies
import ninjaGirl

class Level:
    def __init__(self,chapter):
        self.allEnemies = []
        self.allNinjaGirls = []
        self.allEnemies.clear()
        self.allNinjaGirls.clear()
        self.levelMap = ''
        self.chapter = chapter

    def loadCurrentLevel(self):
        levels = json.loads(self.load_Levels())
        for level in levels['Levels']:
            if level['Level'] == self.chapter:
                self.levelMap = level['Map']
                levelEnimies = level['Eniemes']
                
                for badguys in levelEnimies:
                    for entities in badguys['Entities']:
                        #"Height":200,"DelayStart":3,"FreqSecs":10,"Direction":"Right","Speed":5,"Size":30
                        if badguys['Type'] == "NinjaGirl":
                            self.allNinjaGirls.append(entities)
                        else:
                            badguy = enemies.Enemies(badguys['Type'],entities['DelayStart'],entities['FreqSecs'],entities['Height'],
                                entities['Direction'],entities['Speed'],entities['Size'],entities['Set'])
                            self.allEnemies.append(badguy)
                break

    def load_Levels(self):
        # loads a screen map from file
        f = open('levels.json','r')
        data = f.read()
        data = data.replace('\n','')
        data = data.replace(' ','')
        f.close()

        return data
