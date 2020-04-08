class Mission(object):
    def __init__(self, enemySpaceship, reward):
        self.enemySpaceship = enemySpaceship
        self.success = False
        self.reward = reward

    def getEnemySpaceShip(self):
        return self.enemySpaceship

    def getReward(self):
        if(self.getSuccess == True):
            return self.reward

    def getSuccess(self):
        return self.success

    def missionSuccess(self):
        self.success = True