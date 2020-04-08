import math 
import random 
from time import sleep 
from res import *
import pygame
import os
from Battle import Battle
import inputbox
from Spaceship import Spaceship
from Ability import Ability



class BattleScreen(Screen):

    display = None

    def __init__(self, display, enemySpaceship, player, ui):
        Screen.__init__(self, display)
        self.ui = ui
        self.player = player
        self.playerSpaceship = self.player.getSpaceShip()
        self.enemySpaceship = enemySpaceship
        self.display = display
        self.battle = Battle(self.playerSpaceship, enemySpaceship, self.display)
        self.ability1 = Button(self.playerSpaceship.getAbility(0).getAbilityName(), 50, 500, 200, 50)
        self.ability2 = Button(self.playerSpaceship.getAbility(1).getAbilityName(), 300, 500, 200, 50)
        self.ability3 = Button(self.playerSpaceship.getAbility(2).getAbilityName(), 50, 400, 200, 50)
        self.ability4 = Button(self.playerSpaceship.getAbility(3).getAbilityName(), 300, 400, 200, 50)
        self.textWelcome = Text("Battle!", 200, 100, WHITE, "Arial", 50)
        self.drawComponents()

        


        # This is where battle gets initailized 
        


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
        
        self.drawPlayer(600,240)
        self.drawEnemy(-50,-100)
        
        # @will the problem where the ui would turn into non type is messing up here too. If you could keep UI consistent, then this would work as well.
        if self.ui == UI.BATTLE:
        # we have to find a way to only start the battle sequence once the player has gone through profile selection and then has clicked on battle. 
        # rn it runs with battle initialization in battlescreen. find a way to do that and put battlesequence there only 
            self.battle.battleSequence()
            # t
            #after the battle seq is called 
        # if battle seq = 1:
        #   player.nummision =+ the value that comes from the battleseq
        # else:
        #  player.nummision = 0
        #  hook up story 
        

    def drawPlayer(self, x, y):
        if self.player.getMissionNum() == 0:
            playerLvl0 = pygame.image.load('assets/PlayerSpaceship/Lvl0.png')
            self.display.blit(playerLvl0, (x, y))
        if self.player.getMissionNum() == 1:
            playerLvl1 = pygame.image.load('assets/PlayerSpaceship/Lvl1.png')
            self.display.blit(playerLvl1, (x, y))
        if self.player.getMissionNum() == 2:
            playerLvl2 = pygame.image.load('assets/PlayerSpaceship/Lvl2.png')
            self.display.blit(playerLvl2, (x, y))
        if self.player.getMissionNum() == 3:
            playerLvl3 = pygame.image.load('assets/PlayerSpaceship/Lvl3.png')
            self.display.blit(playerLvl3, (x, y))

    def drawEnemy(self, x, y):
        # print(self.player.missionNum)
        if self.player.getMissionNum() == 0:
            enemyLvl0 = "assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl0/" + str(random.choice(os.listdir("assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl0/")))
            enemyLvl0Add = pygame.image.load(enemyLvl0)
            self.display.blit(enemyLvl0Add, (x, y))
            # self.player.missionNum =+ 1
        if self.player.getMissionNum() == 1:
            enemyLvl1 = "assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl1/" + str(random.choice(os.listdir("assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl1/")))
            enemyLvl1Add = pygame.image.load(enemyLvl1)
            self.display.blit(enemyLvl1Add, (x, y))
            # self.player.missionNum =+ 1
        if self.player.getMissionNum() == 2:
            enemyLvl2 = "assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl2/" + str(random.choice(os.listdir("assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl2/")))
            enemyLvl2Add = pygame.image.load(enemyLvl2)
            self.display.blit(enemyLvl2Add, (x, y))
            # self.player.missionNum =+ 1
        if self.player.getMissionNum() == 3:
            enemyLvl3 = "assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl3/" + str(random.choice(os.listdir("assets/GraphicsAssetSpaceships/PNG/Spaceships/Lvl3/")))
            enemyLvl3Add = pygame.image.load(enemyLvl3)   
            self.display.blit(enemyLvl3Add, (x, y))
            # self.player.missionNum =+ 1 
 
    # @staticmethod
    # def inputHandler():
    #     n = 0
    #     n = int(inputbox.ask(display, 'Message')) #inp will equal whatever the input is
    #     input("Press Enter to continue...")

    #     return n




 
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
    
    def getDisplay(self):
        return self.display
