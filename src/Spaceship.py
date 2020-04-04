import AbilityBuff

class Spaceship(object):

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

    def getMaxHealth(self):
        return self.maxHealth
    
    def getCurrentHealth(self):
        return self.currentHealth

    # Setter Methods
    def takeDamage(self, damage):
        self.currentHealth -= damage
    
    def resetHealth(self):
        self.currentHealth = self.maxHealth

    def setBuff(self, buff):
        self.currentBuff = buff

    def setAbilityCooldown(self, i):
        self.abilityList[i].setCoolDown()

    def setAttackDmg(self, damage):
        self.attackDmg = damage

