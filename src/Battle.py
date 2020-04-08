from enum import Enum

import Spaceship
import Ability
from res import *
import pygame
import inputbox
import string
import random

class Turn(Enum):
    OPPONENT = 1
    PLAYER = 0

class Battle():

    def __init__(self, playerShip, enemyShip, display):
        self.currentTurn = Turn.PLAYER
        self.playerShip = playerShip
        self.enemyShip = enemyShip
        self.battleInProgress = True
        self.playerWin = False
        self.display = display


    def battleSequence(self):

        turnCounter = 0
        # Wait until battle is over
        while(self.battleInProgress):
            # Code used to test in console
            turnCounter = turnCounter + 1
            print("Turn " + str(turnCounter) + " " + str(self.currentTurn))
            self.checkStats(self.playerShip)
            self.checkStats(self.enemyShip)

            # Applying buffs

            if(self.currentTurn == Turn.PLAYER):
                self.applyBuffs(self.playerShip)
            else:
                self.applyBuffs(self.enemyShip)

            # When it is the players turn
            if(self.currentTurn == Turn.PLAYER):
                # First reduce cooldowns
                self.reduceCooldowns(self.playerShip)
                # SELECT A MOVE USING UI
                move = int(inputbox.ask(self.display, 'Move Number')) #inp will equal whatever the input is
                print(move)
                while(self.moveIsValid(move, self.playerShip) == False):
                    # SELECT NEW MOVE IF ABILITY IS ON COOLDOWN
                    print("Move on cool down!")
                    move = int(inputbox.ask(self.display, 'Move Number')) #inp will equal whatever the input is

                self.attack(move, self.playerShip, self.enemyShip)

            # When it is the computers turn
            else:
                # First reduce cooldowns
                self.reduceCooldowns(self.enemyShip)
                # SELECT A MOVE USING UI
                move = random.randrange(0,4)
                while(self.moveIsValid(move, self.enemyShip) == False):
                    # SELECT NEW MOVE IF ABILITY IS ON COOLDOWN
                    print("Move on cool down!")
                    move = random.randrange(0,4)
                self.attack(move, self.enemyShip, self.playerShip)
            
            self.switchTurns()
            self.checkIfBattleEnds()

        return self.playerWin

    def applyBuffs(self, ship):
        
        stunned = False

        for i in ship.getBuffList():
            if(i[0] == Buff.HEAL):
                print("Ship is healing!")
                ship.repairDamage(i[1])
            elif(i[0] == Buff.STUN):
                print("Ship is stunned!")
                self.switchTurns()
                buffRemove = i
                stunned = True
                
            elif(i[0] == Buff.ONFIRE):
                print("Ship is on fire!")
                ship.takeDamage(i[1])

        if(stunned == True):
            ship.removeBuff(buffRemove)
            stunned = False

    def setBuff(self, buff, ship1, ship2):
        if(buff[0] == Buff.HEAL):
            # Repairing removes all debuffs
            ship1.removeAllBuffs()
            ship1.addBuff(buff)
        elif(buff[0] == Buff.STUN):
            ship2.addBuff(buff)
        elif(buff[0] == Buff.ONFIRE):
            # On fire removes all debuffs
            ship1.removeAllBuffs()
            ship2.addBuff(buff)

    def moveIsValid(self, move, ship):
        if(ship.getAbility(move).getCurrentCoolDown() == 0):
            return True
        else:
            return False
        
    def switchTurns(self):

        if(self.currentTurn == Turn.PLAYER):
            self.currentTurn = Turn.OPPONENT
        else:
            self.currentTurn = Turn.PLAYER

    def checkIfBattleEnds(self):
        if(self.playerShip.getCurrentHealth() <= 0):
            self.battleInProgress = False
        elif(self.enemyShip.getCurrentHealth() <= 0):
            self.battleInProgress = False
            self.playerWin = True

    def reduceCooldowns(self, ship):

        ship.reduceAllCooldowns()

    def getEnemySpaceship(self):
        return self.enemyShip

    def getPlayerSpaceship(self):
        return self.playerShip

    def attack(self, move, ship1, ship2):
        if(move == 0):
            ship2.takeDamage(ship1.getAutoDamage())
            print("Using autoattack")
        elif(move == 1):
            ship2.takeDamage(ship1.getAbility(0).getAbilityDamage())
            self.setBuff(ship1.getAbility(0).getAbilityBuff(), ship1, ship2)
            ship1.setAbilityCoolDown(0)
            print("Using " + self.playerShip.getAbility(0).getAbilityName())
        elif(move == 2):
            ship2.takeDamage(ship1.getAbility(1).getAbilityDamage())
            self.setBuff(ship1.getAbility(1).getAbilityBuff(), ship1, ship2)
            ship1.setAbilityCoolDown(1)
            print("Using "  + self.playerShip.getAbility(1).getAbilityName())
        elif(move == 3):
            ship2.takeDamage(ship1.getAbility(2).getAbilityDamage())
            self.setBuff(ship1.getAbility(2).getAbilityBuff(), ship1, ship2)
            ship1.setAbilityCoolDown(2)
            print("Using " + self.playerShip.getAbility(2).getAbilityName())
        else:
            ship2.takeDamage(ship1.getAbility(3).getAbilityDamage())
            self.setBuff(ship1.getAbility(3).getAbilityBuff(), ship1, ship2)
            ship1.setAbilityCoolDown(3)
            
            print("Using " + self.playerShip.getAbility(3).getAbilityName())

    # Used to test in console
    def checkStats(self, ship):
        print("Current Health: " + str(ship.getCurrentHealth()))
        print("Current Buff: " + str(ship.getBuffList()))
        print("Cooldown 1: " + str(ship.getAbilityCoolDown(0)))
        print("Cooldown 2: " + str(ship.getAbilityCoolDown(1)))
        print("Cooldown 3: " + str(ship.getAbilityCoolDown(2)))
        print("Cooldown 4: " + str(ship.getAbilityCoolDown(3)))

#####################################################################################
#####################################  TO DO #####################################
#####################################################################################

# Add ability hit chance
# Add ability buff handling
# Add ability buff cooldown handling
# Add ability cooldown handling

# FIX HOW TO HANDLE BUFF COOLDOWNS

#####################################################################################
#####################################  TESTING  #####################################
#####################################################################################

# ability1 = Ability.Ability(50, (AbilityBuff.Buff.NOBUFF,0, 0), 2, "Hyper Cannnon", 0.8, 50)
# ability2 = Ability.Ability(0, (AbilityBuff.Buff.HEAL,30,2), 3, "Repairs", 1, 50)
# ability3 = Ability.Ability(20, (AbilityBuff.Buff.STUN,0,2), 4, "Stun Move", 0.5, 50)
# ability4 = Ability.Ability(30, (AbilityBuff.Buff.ONFIRE,10,2), 4, "Heat Seeking Missles", 1, 50)

# ability5 = Ability.Ability(50, (AbilityBuff.Buff.NOBUFF,0,0), 2, "Hyper Cannnon", 0.8, 50)
# ability6 = Ability.Ability(0, (AbilityBuff.Buff.HEAL,30,2), 3, "Repairs", 1, 50)
# ability7 = Ability.Ability(20, (AbilityBuff.Buff.STUN,0,2), 4, "Stun Move", 0.5, 50)
# ability8 = Ability.Ability(30, (AbilityBuff.Buff.ONFIRE,10,2), 4, "Heat Seeking Missles", 1, 50)

# abilityList = [ability1, ability2, ability3, ability4]
# abilityList2 = [ability5, ability6, ability7, ability8]

# user = Spaceship.Spaceship(100, 10, abilityList)
# computer = Spaceship.Spaceship(100, 10, abilityList2)

# battleMode = Battle(user, computer)

# playerWin = battleMode.battleSequence()

