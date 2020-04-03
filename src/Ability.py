class Ability():

    def __init__(self, damage, abilityBuff, coolDown):
        self.damage = damage
        self.abilityBuff = abilityBuff
        self.coolDown = coolDown
        self.currentCoolDown = 0

    def getDamage(self):
        return self.damage

    def getAbilityBuff(self):
        return self.abilityBuff

    def getCoolDown(self):
        return self.coolDown
    
    def getCurrentCoolDown(self):
        return self.currentColdDown

    def setCoolDown(self):
        self.currentColdDown = self.coolDown

    def reduceCoolDown(self):
        if(self.currentColdDown != 0):
            self.currentColdDown -= 1

    