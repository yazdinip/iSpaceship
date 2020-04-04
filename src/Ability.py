class Ability(object):

    def __init__(self, damage, abilityBuff, coolDown, abilityName, hitChance):
        self.damage = damage
        self.abilityBuff = abilityBuff
        self.coolDown = coolDown
        self.currentCoolDown = 0
        self.abilityName = abilityName
        self.hitChance = hitChance

    def getAbilityDamage(self):
        return self.damage

    def getAbilityBuff(self):
        return self.abilityBuff

    def getCoolDown(self):
        return self.coolDown
    
    def getCurrentCoolDown(self):
        return self.currentCoolDown

    def getAbilityName(self):
        return self.abilityName
    
    def getHitChance(self):
        return self.hitChance

    def setCoolDown(self):
        self.currentCoolDown = self.currentCoolDown + self.coolDown

    def reduceCoolDown(self):
        if(self.currentCoolDown != 0):
            self.currentCoolDown -= 1

    