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
        return self.currentColdDown

    def getAbilityName(self):
        return self.abilityName
    
    def getHitChance(self):
        return self.hitChance

    def setCoolDown(self):
        self.currentColdDown = self.coolDown

    def reduceCoolDown(self):
        if(self.currentColdDown != 0):
            self.currentColdDown -= 1

    