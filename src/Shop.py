from res import Buff
import Ability

class Shop():

    #itemListA, itemListB, currency, abilityList

    def __init__(self, player):

        # self.player = player

        # self.abilitySwap = 0

        # self.currentDisplayedAItem = itemListA[0]
        # self.indexA = 0
        # self.currentDisplayedBItem = itemListB[0]
        # self.indexB = 0

        # self.abilityIndex = 0
        self.counter = 0

    #return (self.itemListA, self.itemListB, self.currency, self.abilityList)
    def getCounter(self):
        return self.counter

    def setCounter(self, n):
        self.counter = n 
        return self.counter    
        
    def getCurrentA(self):
        return self.currentDisplayedAItem

    def getCurrentB(self):
        return self.currentDisplayedBItem

    def getCurrency(self):
        return self.currency

    def setAbilityIndex(self, n):
        self.abilityIndex = n
        return self.abilityIndex
        
    def getAbilityIndex(self):
        return self.abilityIndex

    def getAbilityList(self):
        return self.abilityList

    def getItemListA(self):
        return self.itemListA
    
    def getItemListB(self):
        return self.itemListB

    def nextA(self):
        if(self.indexA != len(self.itemListA)-1):
            self.currentDisplayedAItem = self.itemListA[self.indexA+1]
            self.indexA += 1

    def prevA(self):
        if(self.indexA != 0):
            self.currentDisplayedAItem = self.itemListA[self.indexA-1]
            self.indexA += -1

    def nextB(self):
        if(self.indexB != len(self.itemListB)-1):
            self.currentDisplayedBItem = self.itemListB[self.indexB+1]
            self.indexB += 1

    def prevB(self):
            self.currentDisplayedAItem = self.itemListA[0]
            self.currentDisplayedBItem = self.itemListB[self.indexB-1]
            self.indexB += -1

    def buy(self):
        # Check if player has sufficient funds
        if(self.currency >= self.currentDisplayedAItem.getPrice()):
            # Deduct funds
            self.currency = self.currency - self.currentDisplayedAItem.getPrice()
            # Take out item from avaiable list
            swappedItem = self.itemListA.pop(self.indexA)
            # Add to bought list
            self.itemListB.append(swappedItem)
            # Update current item to beginning of list
            self.currentDisplayedAItem = self.itemListA[0]
            self.indexA = 0
        else:
            print("Insufficient Funds")

    def equip(self):

        tempAbility = self.abilityList[self.abilityIndex]

        # Replace ability slot with item in question
        self.abilityList[self.abilityIndex] = self.itemListB[self.indexB]

        # Add temp ability back into list B
        self.itemListB.insert(self.indexB+1,tempAbility)
        #self.itemListB.append(tempAbility)

        self.itemListB.pop(self.indexB)

        # Change display
        self.currentDisplayedBItem = self.itemListB[0]
        self.indexB = 0

    def check(self):
        print("Money: " + str(self.currency))
        print(self.itemListA)
        print(self.itemListB)
        print("ARSENAL")
        print(self.abilityList)
        print("Current Item Ava: " + self.currentDisplayedAItem.getAbilityName())
        print("Current Item Bou: " + self.currentDisplayedBItem.getAbilityName())

    @staticmethod
    def getAbilities():

        ability1 = Ability.Ability(50, (Buff.NOBUFF,0, 0), 2, "Hyper Cannnon", 0.8, 50)
        ability2 = Ability.Ability(0, (Buff.HEAL,30,2), 3, "Repairs", 1, 50)
        ability3 = Ability.Ability(20, (Buff.STUN,0,2), 4, "Stun Move", 0.5, 50)
        ability4 = Ability.Ability(30, (Buff.ONFIRE,10,2), 4, "Heat Seeking Missles", 1, 50)

        ability5 = Ability.Ability(50, (Buff.NOBUFF,0,0), 2, "YESSIR", 0.8, 50)
        ability6 = Ability.Ability(0, (Buff.HEAL,30,2), 3, "ESKEGIT", 1, 500)
        ability7 = Ability.Ability(20, (Buff.STUN,0,2), 4, "YEET", 0.5, 50)
        ability8 = Ability.Ability(30, (Buff.ONFIRE,10,2), 4, "LMAO", 1, 50)

        ability9 = Ability.Ability(50, (Buff.NOBUFF,0,0), 2, "BRUH", 0.8, 50)
        ability10 = Ability.Ability(0, (Buff.HEAL,30,2), 3, "NAWWW", 1, 500)
        ability11 = Ability.Ability(20, (Buff.STUN,0,2), 4, "JHEEEZ", 0.5, 50)
        ability12 = Ability.Ability(30, (Buff.ONFIRE,10,2), 4, "BLESSED", 1, 50)

        allAbilities = [ability1, ability2, ability3, ability4, ability5, ability6, ability7, ability8, ability9, ability10, ability11, ability12]
        return  (allAbilities)

#list a is available 
#list b is bought 
#ability list is equipped


#shopMode = Shop(abilityListA, abilityListB, currency, abilityList)

#shopMode.check()

#shopMode.equip()

#shopMode.check()