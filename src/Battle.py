from enum import Enum

import Spaceship
import Ability
import AbilityBuff
import random

class Turn(Enum):
    OPPONENT = 1
    PLAYER = 0


class Battle():
    def __init__(self, playerShip, enemyShip):

        self.currentTurn = Turn.PLAYER

        self.playerShip = playerShip
        self.enemyShip = enemyShip

        self.battleInProgress = True

    def battleSequence(self):
        
        # Wait until battle is over
        while(self.battleInProgress):
            # When it is the players turn
            if(self.currentTurn == Turn.PLAYER):
                # REPLACE RANDOM WITH UI INPUT
                move = random.randrange(0,4)
                self.attack(move)

            # When it is the computers turn
            else:
                move = random.randrange(0,4)
                self.attack(move)
        
    def switchTurns(self):
        if(self.currentTurn == Turn.PLAYER):
            self.currentTurn = Turn.OPPONENT
        else:
            self.currentTurn = Turn.PLAYER

    def attack(self, move):
        if(self.currentTurn == Turn.PLAYER):
            if(move == 0):
                self.enemyShip.takeDamage(self.playerShip.getAutoDamage())
                print("Player attacks enemy using autoattack")
            elif(move == 1):
                self.enemyShip.takeDamage(self.playerShip.getAbility(0).getAbilityDamage())
                self.playerShip.setAbilityCoolDown(0)
                print("Player attacks enemy using " + self.playerShip.getAbility(0).getAbilityName())
            elif(move == 2):
                self.enemyShip.takeDamage(self.playerShip.getAbility(1).getAbilityDamage())
                self.playerShip.setAbilityCoolDown(1)
                print("Player attacks enemy using "  + self.playerShip.getAbility(1).getAbilityName())
            elif(move == 3):
                self.enemyShip.takeDamage(self.playerShip.getAbility(2).getAbilityDamage())
                self.playerShip.setAbilityCoolDown(2)
                print("Player attacks enemy using " + self.playerShip.getAbility(2).getAbilityName())
            else:
                self.enemyShip.takeDamage(self.playerShip.getAbility(3).getAbilityDamage())
                self.playerShip.setAbilityCoolDown(3)
                print("Player attacks enemy using " + self.playerShip.getAbility(3).getAbilityName())
        
        else:
            if(move == 0):
                self.playerShip.takeDamage(self.enemyShip.getAutoDamage())
                print("Enemy attacks player using autoattack")
            elif(move == 1):
                self.playerShip.takeDamage(self.enemyShip.getAbility(0).getAbilityDamage())
                self.enemyShip.setAbilityCoolDown(0)
                print("Enemy attacks player using " + self.enemyShip.getAbility(0).getAbilityName())
            elif(move == 2):
                self.playerShip.takeDamage(self.enemyShip.getAbility(1).getAbilityDamage())
                self.enemyShip.setAbilityCoolDown(1)
                print("Enemy attacks player using " + self.enemyShip.getAbility(1).getAbilityName())
            elif(move == 3):
                self.playerShip.takeDamage(self.enemyShip.getAbility(2).getAbilityDamage())
                self.enemyShip.setAbilityCoolDown(2)
                print("Enemy attacks player using " + self.enemyShip.getAbility(2).getAbilityName())
            else:
                self.playerShip.takeDamage(self.enemyShip.getAbility(3).getAbilityDamage())
                self.enemyShip.setAbilityCoolDown(3)
                print("Enemy attacks player using " + self.enemyShip.getAbility(3).getAbilityName())

#####################################################################################
#####################################  TO DO #####################################
#####################################################################################

# Add ability hit chance
# Add ability buff handling
# Add ability cooldown handling

#####################################################################################
#####################################  TESTING  #####################################
#####################################################################################

def checkStats(ship):
            print("Current Health: ", ship.getCurrentHealth())
            print("Current Buff: ", ship.getCurrentBuff())
            print("Cooldown 1: " , ship.getAbilityCoolDown(0))
            print("Cooldown 2: " , ship.getAbilityCoolDown(1))
            print("Cooldown 3: " , ship.getAbilityCoolDown(2))
            print("Cooldown 4: " , ship.getAbilityCoolDown(3))

ability1 = Ability.Ability(50, AbilityBuff.Buff.NOBUFF, 2, "Hyper Cannnon", 0.8)
ability2 = Ability.Ability(0, AbilityBuff.Buff.HEAL, 3, "Heal Thyself", 1)
ability3 = Ability.Ability(20, AbilityBuff.Buff.STUN, 4, "Stun Move", 0.5)
ability4 = Ability.Ability(30, AbilityBuff.Buff.NOBUFF, 4, "Heat Seeking Missles", 1)

ability5 = Ability.Ability(50, AbilityBuff.Buff.NOBUFF, 2, "Hyper Cannnon", 0.8)
ability6 = Ability.Ability(0, AbilityBuff.Buff.HEAL, 3, "Heal Thyself", 1)
ability7 = Ability.Ability(20, AbilityBuff.Buff.STUN, 4, "Stun Move", 0.5)
ability8 = Ability.Ability(30, AbilityBuff.Buff.NOBUFF, 4, "Heat Seeking Missles", 1)

abilityList = [ability1, ability2, ability3, ability4]
abilityList2 = [ability5, ability6, ability7, ability8]

user = Spaceship.Spaceship(100, 10, abilityList)
computer = Spaceship.Spaceship(100, 10, abilityList2)

battleMode = Battle(user, computer)

checkStats(user)
checkStats(computer)

battleMode.attack(0)
checkStats(user)
checkStats(computer)
battleMode.switchTurns()

battleMode.attack(1)
checkStats(user)
checkStats(computer)
battleMode.switchTurns()

battleMode.attack(2)
checkStats(user)
checkStats(computer)
battleMode.switchTurns()


battleMode.attack(3)
checkStats(user)
checkStats(computer)
battleMode.switchTurns()

checkStats(user)
checkStats(computer)
battleMode.switchTurns()



