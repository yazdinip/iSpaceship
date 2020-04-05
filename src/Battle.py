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
        self.playerWin = False

    def battleSequence(self):
        
        # Wait until battle is over
        while(self.battleInProgress):

            # When it is the players turn
            if(self.currentTurn == Turn.PLAYER):
                # REPLACE RANDOM WITH UI INPUT
                move = random.randrange(0,4)
                self.attack(move, self.playerShip, self.enemyShip)

            # When it is the computers turn
            else:
                move = random.randrange(0,4)
                self.attack(move, self.enemyShip, self.playerShip)
            
            self.switchTurns()
            self.reduceCooldowns()
            self.checkIfBattleEnds()

        return self.playerWin
        
    def switchTurns(self):

        if(self.currentTurn == Turn.PLAYER):
            self.currentTurn = Turn.OPPONENT
        else:
            self.currentTurn = Turn.PLAYER

    def checkIfBattleEnds(self):
        if(self.playerShip.getCurrentHealth() == 0):
            self.battleInProgress = False
            self.playerWin = True
        elif(self.enemyShip.getCurrentHealth() == 0):
            self.battleInProgress = False

    def reduceCooldowns(self):

        self.playerShip.reduceAllCooldowns()
        self.enemyShip.reduceAllCooldowns()

    def attack(self, move, ship1, ship2):
        if(move == 0):
            ship2.takeDamage(ship1.getAutoDamage())
            print("Using autoattack")
        elif(move == 1):
            ship2.takeDamage(ship1.getAbility(0).getAbilityDamage())
            ship1.setAbilityCoolDown(0)
            print("Using " + self.playerShip.getAbility(0).getAbilityName())
        elif(move == 2):
            ship2.takeDamage(ship1.getAbility(1).getAbilityDamage())
            ship1.setAbilityCoolDown(1)
            print("Using "  + self.playerShip.getAbility(1).getAbilityName())
        elif(move == 3):
            ship2.takeDamage(ship1.getAbility(2).getAbilityDamage())
            ship1.setAbilityCoolDown(2)
            print("Using " + self.playerShip.getAbility(2).getAbilityName())
        else:
            ship2.takeDamage(ship1.getAbility(3).getAbilityDamage())
            ship1.setAbilityCoolDown(3)
            print("Using " + self.playerShip.getAbility(3).getAbilityName())

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
ability2 = Ability.Ability(0, AbilityBuff.Buff.HEAL, 3, "Repairs", 1)
ability3 = Ability.Ability(20, AbilityBuff.Buff.STUN, 4, "Stun Move", 0.5)
ability4 = Ability.Ability(30, AbilityBuff.Buff.NOBUFF, 4, "Heat Seeking Missles", 1)

ability5 = Ability.Ability(50, AbilityBuff.Buff.NOBUFF, 2, "Hyper Cannnon", 0.8)
ability6 = Ability.Ability(0, AbilityBuff.Buff.HEAL, 3, "Repairs", 1)
ability7 = Ability.Ability(20, AbilityBuff.Buff.STUN, 4, "Stun Move", 0.5)
ability8 = Ability.Ability(30, AbilityBuff.Buff.NOBUFF, 4, "Heat Seeking Missles", 1)

abilityList = [ability1, ability2, ability3, ability4]
abilityList2 = [ability5, ability6, ability7, ability8]

user = Spaceship.Spaceship(100, 10, abilityList)
computer = Spaceship.Spaceship(100, 10, abilityList2)

battleMode = Battle(user, computer)

checkStats(user)
checkStats(computer)

battleMode.attack(0, user, computer)
checkStats(user)
checkStats(computer)

battleMode.attack(1, computer, user)
checkStats(user)
checkStats(computer)

battleMode.attack(2, user, computer)
checkStats(user)
checkStats(computer)

battleMode.attack(3, computer, user)
checkStats(user)
checkStats(computer)

checkStats(user)
checkStats(computer)



