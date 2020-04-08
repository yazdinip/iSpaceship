import Ability
import AbilityBuff

import Spaceship

class Player(object):
    def __init__(self):

        ability1 = Ability.Ability(50, (AbilityBuff.Buff.NOBUFF,0, 0), 2, "Cannnon", 0.8, 20)
        ability2 = Ability.Ability(0, (AbilityBuff.Buff.HEAL,30,2), 3, "Repairs", 1, 50)
        ability3 = Ability.Ability(20, (AbilityBuff.Buff.STUN,0,2), 4, "Stun Move", 0.5, 50)
        ability4 = Ability.Ability(30, (AbilityBuff.Buff.ONFIRE,10,2), 4, "Heat Seeking Missles", 1, 50)

        self.currency = 500

        self.maxHealth = 100

        self.attackDmg = 10

        self.abilityList = [ability1, ability2, ability3, ability4]

        self.missionList = []

        self.abilityListA = []
        self.abilityListB = []

        self.playerSpaceShip = Spaceship.Spaceship(self.maxHealth, self.attackDmg, self.abilityList)

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

    def getMissionList(self):
        return self.missionList

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

    def setAbiltiyListB(self, abilityListB):
        self.abilityListB = abilityListB

    def setSpaceShip (self, spaceship):
        self.playerSpaceShip = spaceship
    
    def setMissionList(self, missionList):
        self.missionList = missionList