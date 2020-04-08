import math 
import random 
from res import *
import pygame
import os
from Battle import Battle
from Spaceship import Spaceship
from Ability import Ability


class BattleScreen(Screen):
    def __init__(self, display, enemySpaceship, player):
        Screen.__init__(self, display)

        
        self.player = player
        self.playerSpaceship = self.player.getSpaceShip()
        self.enemySpaceship = enemySpaceship
        self.battle = Battle(self.playerSpaceship, enemySpaceship)
        self.display = display
        

        self.ability1 = Button(self.playerSpaceship.getAbility(0).getAbilityName(), 50, 500, 200, 50)
        self.ability2 = Button(self.playerSpaceship.getAbility(1).getAbilityName(), 300, 500, 200, 50)
        self.ability3 = Button(self.playerSpaceship.getAbility(2).getAbilityName(), 50, 400, 200, 50)
        self.ability4 = Button(self.playerSpaceship.getAbility(3).getAbilityName(), 300, 400, 200, 50)
        self.textWelcome = Text("Battle!", 200, 100, WHITE, "Arial", 50)

        self.drawComponents()


    def drawComponents(self):
        

        self.textWelcome = Text("Battle!", 300, 25, WHITE, "Arial", 50)

        self.playerHealth = Text("Health: " + str(self.player.getSpaceShip().getCurrentHealth()),450, 350, WHITE, "Arial", 25)

        self.components.clear()
        self.components.append(self.textWelcome)
        self.components.append(self.playerHealth)

        self.components.append(self.ability1)
        self.components.append(self.ability2)
        self.components.append(self.ability3)
        self.components.append(self.ability4)
        
        # self.drawPlayer(0,0)
        self.drawEnemy(0,0)
        
        

    # def drawPlayer(self, x, y):
    #     if self.player.getMissionNum() == 0:
    #         playerLvl1 = pygame.image.load('assets/PlayerSpaceship/Lvl1.png')
    #         self.display.blit(playerLvl1, (x, y))
        # if self.player.getMissionNum == 1:
        #     playerLvl1 = pygame.image.load('assets/PlayerSpaceship/Lvl1.png')
        #     self.display.blit(playerLvl1, (x, y))
        # if self.player.getMissionNum == 2:
        #     playerLvl2 = pygame.image.load('assets/PlayerSpaceship/Lvl2.png')
        #     self.display.blit(playerLvl2, (x, y))
        # if self.player.getMissionNum == 3:
        #     playerLvl3 = pygame.image.load('assets/PlayerSpaceship/Lvl3.png')
        #     self.display.blit(playerLvl3, (x, y))
        # if self.player.getMissionNum == 4:
        #     playerLvl4 = pygame.image.load('assets/PlayerSpaceship/Lvl3.png')
        #     self.display.blit(playerLvl4, (x, y))

    def drawEnemy(self, x, y):
        if self.player.getMissionNum() == 0:
            enemyLvl1 = "assets/GraphicsAssetSpaceships/PNG/Spaceships/01/" + str(random.choice(os.listdir("assets/GraphicsAssetSpaceships/PNG/Spaceships/01/")))
            enemyLvl1Add = pygame.image.load(enemyLvl1)
            self.display.blit(enemyLvl1Add, (x, y))
    #     if player == 2:
    #         enemyLvl2 = pygame.image.load(random.choice(os.listdir("assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl2")))
    #         display.blit(enemyLvl2, (x, y))
    #     if player == 3:
    #         enemyLvl3 = pygame.image.load(random.choice(os.listdir("assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl3//")))
    #         display.blit(enemyLvl3, (x, y))
    #     if player == 4:
    #         enemyLvl4 = pygame.image.load(random.choice(os.listdir("assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl4//")))
    #         display.blit(enemyLvl4, (x, y))      
        

    def checkForComponentClicks(self, ui):
        if self.ability1.isBeingClicked(ui) == True:
                # g = input("Enter your moveT ") rue:
            pass
        # if self.ability2.isBeingClicked(ui) == True:
        #     # Do something
        # if self.abilic) == True:
        #     # Do something
        # if self.ability4.isBeingClicked(ui) == True:
        #     # Do something

    def updateProfile(self, profile):
        self.profile = profile


    def getEnemySpaceship(self):
        return self.enemySpaceship

    def getPlayerSpaceshipself(self):
        return self.playerSpaceship

    def updatePlayer(self, player):
        self.player = player
