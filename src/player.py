import Ability
from res import *
import Story

import Spaceship

class Player(object):
    def __init__(self):
        
        self.currency = 500

        self.maxHealth = 100

        self.attackDmg = 10

        self.abilityList = Story.playerAbilityList

        self.missionNum = 0

        self.itemListA = Story.abilityA
        self.itemListB = Story.abilityB
        self.playerSpaceShip = Spaceship.Spaceship(self.maxHealth, self.attackDmg, self.abilityList)

        self.abilitySwap = 0

        self.currentDisplayedAItem = self.itemListA[0]
        self.indexA = 0
        self.currentDisplayedBItem = self.itemListB[0]
        self.indexB = 0

        self.abilityIndex = 0

    # Getters

    def getCurrency(self):
        return self.currency

    def getAttackDmg(self):
        return self.attackDmg

    def getMaxHealth(self):
        return self.maxHealth

    def getAbilityList(self):
        return self.abilityList

    def getAbilityListA(self):
        return self.abilityListA
    
    def getAbilityListB(self):
        return self.abilityListB

    def getSpaceShip(self):
        return self.playerSpaceShip

    def getMissionNum(self):
        return self.missionNum
    
    # Setters

    def addCurrency(self, amount):
        self.currency = self.currency + amount

    def removeCurrency(self, amount):
        self.currency = self.currency - amount

    def addMaxHealth(self, amount):
        self.maxHealth = self.maxHealth - amount

    def setAbilityList(self, abilityList):
        self.abilityList = abilityList
    
    def setAbiltiyListA(self, abilityListA):
        self.abilityListA = abilityListA
    
    def setCurrency(self, currency):
        self.currency = currency

    def setAbiltiyListB(self, abilityListB):
        self.abilityListB = abilityListB

    def setSpaceShip (self, spaceship):
        self.playerSpaceShip = spaceship
    
    def setMissionNum(self):
        self.missionNum =+ 1

    def resetMissionNum(self):
        self.missionNum = 0 

    def getCurrentA(self):
        return self.currentDisplayedAItem

    def getCurrentB(self):
        return self.currentDisplayedBItem

    def resetHealth(self):
        self.playerSpaceShip.resetHealth()

    def getItemListA(self):
        return self.itemListA
    
    def getItemListB(self):
        return self.itemListB

    def getAbilityIndex(self):
        return self.abilityIndex
    def setAbilityIndex(self, n):
        self.abilityIndex = n

    def nextA(self):
        if(self.indexA != len(self.itemListA)-1):
            self.currentDisplayedAItem = self.itemListA[self.indexA+1]
            self.indexA += 1

    def prevA(self):
        if(self.indexA != 0):
            self.currentDisplayedAItem = self.itemListA[self.indexA-1]
            self.indexA += -1

    def nextB(self):
        if(self.indexB != len(self.itemListB)-1):
            self.currentDisplayedBItem = self.itemListB[self.indexB+1]
            self.indexB += 1

    def prevB(self):
        if(self.indexB != 0):
            self.currentDisplayedBItem = self.itemListB[self.indexB-1]
            self.indexB += -1

    def buy(self):
        # Check if player has sufficient funds
        if(self.currency >= self.currentDisplayedAItem.getPrice()):
            # Deduct funds
            self.currency = self.currency - self.currentDisplayedAItem.getPrice()
            # Take out item from avaiable list
            swappedItem = self.itemListA.pop(self.indexA)
            # Add to bought list
            self.itemListB.append(swappedItem)
            # Update current item to beginning of list
            self.currentDisplayedAItem = self.itemListA[0]
            self.indexA = 0
        else:
            print("Insufficient Funds")
            

    def equip(self):

        tempAbility = self.abilityList[self.abilityIndex]

        # Replace ability slot with item in question
        self.abilityList[self.abilityIndex] = self.itemListB[self.indexB]

        # Add temp ability back into list B
        self.itemListB.insert(self.indexB+1,tempAbility)
        #self.itemListB.append(tempAbility)

        self.itemListB.pop(self.indexB)

        # Change display
        self.currentDisplayedBItem = self.itemListB[0]
        self.indexB = 0

