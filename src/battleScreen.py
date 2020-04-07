import math 
import random 
from res import *
import pygame
import Battle
import Spaceship
import Buff
import Ability


class BattleScreen(Screen):
    def __init__(self, display, enemySpaceship, playerSpaceship):
        Screen.__init__(self, display)
        self.SpaceshipPlayer = playerSpaceship
        self.enemySpaceship = enemySpaceship
        self.battle = Battle(playerSpaceship, enemySpaceship)
        self.display = display


        self.ability1 = Button("Ability 1", 100, 375, 100, 50)
        self.ability2 = Button("Ability 2", 175, 375, 100, 50)
        self.ability3 = Button("Ability 3", 100, 300, 100, 50)
        self.ability4 = Button("Ability 4", 175, 300, 100, 50)
        self.textWelcome = Text("Battle!", 200, 100, WHITE, "Arial", 50)


    def drawComponents(self):

        playerString = "Health: " + str(playerSpaceship.getCurrentHealth() + "\n" + "Buff: " + str(playerSpaceShip.getBuffList()))


        self.textWelcome = Text("Battle!", 200, 100, WHITE, "Arial", 50)

        self.components.clear()     # Clear components before drawing them
        self.components.append(self.textWelcome)
        self.components.append(self.ability1)
        self.components.append(self.ability2)
        self.components.append(self.ability3)
        self.components.append(self.ability4)

    def player(x, y):
        display.blit(playerImg, (x, y))

    def checkForComponentClicks(self, ui):
        if self.ability1.isBeingClicked(ui) == True:
            
        # if self.ability2.isBeingClicked(ui) == True:
        #     # Do something
        # if self.ability3.isBeingClicked(ui) == True:
        #     # Do something
        # if self.ability4.isBeingClicked(ui) == True:
        #     # Do something

    def updateProfile(self, profile):
        self.profile = profile
        self.init()