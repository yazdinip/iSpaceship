import math 
import random 
from res import *
import pygame
import os
from Battle import Battle
from Spaceship import Spaceship
from Ability import Ability


class BattleScreen(Screen):
    def __init__(self, display, enemySpaceship, playerSpaceship):
        Screen.__init__(self, display)

        self.playerSpaceship = playerSpaceship
        self.enemySpaceship = enemySpaceship
        self.battle = Battle(playerSpaceship, enemySpaceship)
        self.display = display
        # self.player = player

        self.ability1 = Button(self.playerSpaceship.getAbility(0).getAbilityName(), 50, 500, 200, 50)
        self.ability2 = Button(self.playerSpaceship.getAbility(1).getAbilityName(), 300, 500, 200, 50)
        self.ability3 = Button(self.playerSpaceship.getAbility(2).getAbilityName(), 50, 400, 200, 50)
        self.ability4 = Button(self.playerSpaceship.getAbility(3).getAbilityName(), 300, 400, 200, 50)
        self.textWelcome = Text("Battle!", 200, 100, WHITE, "Arial", 50)

        # self.drawPlayer(display, 1, 0, 0)
        self.drawComponents()


    # def g = input("Press Enter to Start Battle ") 
    # 
    def drawComponents(self):
        # playerString = "Health: " + s

        self.textWelcome = Text("Battle!", 200, 100, WHITE, "Arial", 50)
        self.components.clear()
        self.components.append(self.textWelcome)
        self.components.append(self.ability1)
        self.components.append(self.ability2)
        self.components.append(self.ability3)
        self.components.append(self.ability4)
        # self.drawPlayer(self.display, 1, 100, 100)
        playerLvl1 = pygame.image.load('assets/img/enemy.png')
        self.display.blit(playerLvl1, (0, 0))
        #self.display.update(self.display.blit(playerLvl1, (100, 100)))
        

    # def drawPlayer(self, display, player, x, y):
    #     if player == 1:
    #         playerLvl1 = pygame.image.load('assets/SpaceshipAssetEnemy/enemy-attack.png')
    #         self.display.blit(playerLvl1, (x, y))

    #     if player == 2:
    #         playerLvl2 = pygame.image.load('assets/PlayerSpaceship/Lvl2.png')
    #         self.display.blit(playerLvl2, (x, y))
    #     if player == 3:
    #         playerLvl3 = pygame.image.load('assets/PlayerSpaceship/Lvl3.png')
    #         self.display.blit(playerLvl3, (x, y))
    #     if player == 4:
    #         playerLvl4 = pygame.image.load('assets/PlayerSpaceship/Lvl3.png')
    #         self.display.blit(playerLvl4, (x, y))

    # def drawEnemy(player, x, y):
    #     if player == 1:
    #         enemyLvl1 = pygame.image.load(random.choice(os.listdir("assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl1//")))
    #         display.blit(enemyLvl1, (x, y))
    #     if player == 2:
    #         enemyLvl2 = pygame.image.load(random.choice(os.listdir("assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl2//")))
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
        self.init()

    def getEnemySpaceship(self):
        return self.enemySpaceship

    def getPlayerSpaceshipself():
        return self.playerSpaceship
