import AbilityBuff

class Spaceship(object):

    def __init__(self, maxHealth, attackDmg, abilityList):

        self.maxHealth = maxHealth
        self.currentHealth = maxHealth

        self.currentBuff = set()

        self.attackDmg = attackDmg

        self.abilityList = abilityList

    # Getter Methods 

    def getAutoDamage(self):
        return self.attackDmg

    def getAbility(self, i):
        return self.abilityList[i]

    def getMaxHealth(self):
        return self.maxHealth
    
    def getCurrentHealth(self):
        return self.currentHealth

    def getAbilityCoolDown(self, i):
        return self.abilityList[i].getCurrentCoolDown()

    def getBuffList(self):
        return self.currentBuff

    # Setter Methods

    def removeAllBuffs(self):
        self.currentBuff = set()

    def removeBuff(self, buff):
        self.currentBuff.remove(buff)

    def repairDamage(self, amount):
        # Overhealing is allowed
        self.currentHealth = self.currentHealth + amount

    def takeDamage(self, damage):
        self.currentHealth = self.currentHealth - damage
    
    def resetHealth(self):
        self.currentHealth = self.maxHealth

    def setAbilityCoolDown(self, i):
        self.abilityList[i].setCoolDown()

    def setAttackDmg(self, damage):
        self.attackDmg = damage
    
    def addBuff (self, buff):
        self.currentBuff.add(buff)

    def reduceAllCooldowns(self):
        for i in range(0, 3):
            self.abilityList[i].reduceCoolDown()

