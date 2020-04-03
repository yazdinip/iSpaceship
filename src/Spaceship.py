import AbilityBuff

class Spaceship():

    def __init__(self, maxHealth, attackDmg, abilityList):

        self.maxHealth = maxHealth
        self.currentHealth = maxHealth

        self.currentBuff = AbilityBuff.Buff.NOBUFF

        self.attackDmg = attackDmg

        self.abilityList = abilityList

    # Getter Methods 
    def getAutoDamage(self):
        return self.attackDmg
    
    def getCurrentBuff(self):
        return self.currentBuff

    def getAbility(self, i):
        return self.abilityList[i]

    # Setter Methods
    def takeDamage(self, damage):
        self.currentHealth -= damage
    
    def resetHealth(self):
        self.currentHealth = self.maxHealth

    def setBuff(self, buff):
        self.currentBuff = buff

    def setAttackDmg(self, damage):
        self.attackDmg = damage

