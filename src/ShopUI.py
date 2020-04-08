from res import *
#import pygbutton
#import pygame
from Shop import Shop

# allAbilities = Shop.getAbilities()
# abilityListA = allAbilities[0:3]
# abilityListB = allAbilities[4:7]
# abilityList = allAbilities[7:11]
# currency = 200
# shopMode = Shop(abilityListA, abilityListB, currency, abilityList)
#print(shopMode.currentDisplayedAItem)
#print(shopMode.currentDisplayedAItem.getAbilityName())
#shopMode.nextA()
#print(shopMode.currentDisplayedAItem)

class ShopUI(Screen):
    def __init__(self, display, player):
        Screen.__init__(self, display)
        #self.Item = Item 
        self.player = player
        self.init()
    
    def init(self):
         
        # Create the components of the main screen

        self.wallet = Text(f"You have ${self.player.getCurrency()}!" , 400, 50, WHITE, "Arial", 25)
        self.item_name = Text("Name: " + self.player.getCurrentA().getAbilityName(), 100, 100, WHITE, "Arial", 20)
        self.item_price = Text("Price: " + str(self.player.getCurrentA().getPrice())+"$", 100, 130, WHITE, "Arial", 20)
        self.item_damage = Text("Damage: " + str(self.player.getCurrentA().getAbilityDamage()), 100, 160, WHITE, "Arial", 20)
        
        self.item_cool_down = Text("Cool Down: " + str(self.player.getCurrentA().getCoolDown())+"s", 100, 190, WHITE, "Arial", 20)
        self.item_hit_chance = Text("Hit Chance: " + str(self.player.getCurrentA().getHitChance()*10)+"%", 100, 220, WHITE, "Arial", 20)
        
        #Buy: Section
        self.prev_buy = Button("Previous Item", 400, 100, 150, 50)
        self.next_buy = Button("Next Item", 600, 100, 100, 50)
        self.buy = Button("Buy Item", 500, 200, 100, 50)

        #Bought: Section
        self.item_bought_name = Text("Name: " + self.player.getCurrentB().getAbilityName(), 100, 300, WHITE, "Arial", 20)
        self.item_bought_price = Text("Price: " + str(self.player.getCurrentB().getPrice())+"$", 100, 330, WHITE, "Arial", 20)
        self.item_bought_damage = Text("Damage: " + str(self.player.getCurrentB().getAbilityDamage()), 100, 360, WHITE, "Arial", 20)
        self.item_bought_cool_down = Text("Cool Down: " + str(self.player.getCurrentB().getCoolDown())+"s", 100, 390, WHITE, "Arial", 20)
        self.item_bought_hit_chance = Text("Hit Chance: " + str(self.player.getCurrentB().getHitChance()*10)+"%", 100, 420, WHITE, "Arial", 20)

        self.prev_bought = Button("Previous Item", 400, 330, 150, 50)
        self.next_bought = Button("Next Item", 600, 330, 100, 50)
        self.swap = Button("Swap Item",500 , 400, 100, 50)

        #Abilities Section
        self.item_equipped1 = Button(self.player.getAbilityList()[0].getAbilityName(),100 , 510, 80, 60)
        self.item_equipped2 = Button(self.player.getAbilityList()[1].getAbilityName(),200 , 510, 80, 60)
        self.item_equipped3 = Button(self.player.getAbilityList()[2].getAbilityName(),300 , 510, 80, 60)
        self.item_equipped4 = Button(self.player.getAbilityList()[3].getAbilityName(),400 , 510, 80, 60)

        self.item_details = Text(f"Ability Details for {self.player.getAbilityList()[self.player.getAbilityIndex()].getAbilityName()} ", 500, 510, WHITE, "Arial", 15)
        self.item_equipped_price = Text("Price: " + str(self.player.getAbilityList()[self.player.getAbilityIndex()].getPrice())+"$", 600, 525, WHITE, "Arial", 12)
        self.item_equipped_damage = Text("Damage: " + str(self.player.getAbilityList()[self.player.getAbilityIndex()].getAbilityDamage()), 600, 540, WHITE, "Arial", 12)
        self.item_equipped_cool_down = Text("Cool Down: " + str(self.player.getAbilityList()[self.player.getAbilityIndex()].getCoolDown())+"s", 600, 555, WHITE, "Arial", 12)
        self.item_equipped_hit_chance = Text("Hit Chance: " + str(self.player.getAbilityList()[self.player.getAbilityIndex()].getHitChance()*10)+"%", 600, 570, WHITE, "Arial", 12)

        #back button
        self.back = Button("Back",650 , 10, 100, 50)
        #self.testButton = pygbutton.PygButton((50, 50, 60, 30), 'Button Caption')
        
        # while True: # main game loop
        #     for event in pygame.event.get(): # event handling loop
        #         if 'click' in buttonObj.handleEvent(event):
        #             pass # Do stuff in response to button click here.
        #testButton.draw(DISPLAYSURFACE) # where DISPLAYSURFACE was the Surface object returned from pygame.display.set_mode()
        
        # Add components to components list
        self.components.clear()     # Clear components before drawing them
        self.components.append(self.prev_buy)
        self.components.append(self.next_buy)
        self.components.append(self.prev_bought)
        self.components.append(self.next_bought)
        self.components.append(self.buy)
        self.components.append(self.swap)
        self.components.append(self.back)
        self.components.append(self.wallet)

        self.components.append(self.item_equipped1)
        self.components.append(self.item_equipped2)
        self.components.append(self.item_equipped3)
        self.components.append(self.item_equipped4)

        self.components.append(self.item_name)
        self.components.append(self.item_price)
        self.components.append(self.item_damage)
        self.components.append(self.item_cool_down)
        self.components.append(self.item_hit_chance)

        self.components.append(self.item_bought_name)
        self.components.append(self.item_bought_price)
        self.components.append(self.item_bought_damage)
        self.components.append(self.item_bought_cool_down)
        self.components.append(self.item_bought_hit_chance)

        self.components.append(self.item_equipped_price)
        self.components.append(self.item_equipped_damage)
        self.components.append(self.item_equipped_cool_down)
        self.components.append(self.item_equipped_hit_chance)

        self.components.append(self.item_details)        
        # self.components.append(self.testButton)
        

 
    def checkForComponentClicks(self, ui):
        if self.prev_buy.isBeingClicked(ui) == True:
            self.player.prevA()
        elif self.next_buy.isBeingClicked(ui) == True:
            self.player.nextA()
            #self.playerUI.init()
#            print(self.player.getCurrentA().getAbilityName())
#            pygame.display.update()
#            self.item_name = Text("Name: " + self.player.getCurrentA().getAbilityName(), 100, 100, WHITE, "Arial", 20)
            #i = ui.player
        elif self.next_bought.isBeingClicked(ui) == True:
            self.player.nextB()
        elif self.prev_bought.isBeingClicked(ui) == True:
            self.player.prevB()
        elif self.buy.isBeingClicked(ui) == True:
            self.player.buy()
        elif self.swap.isBeingClicked(ui) == True:
            self.player.equip()
        elif self.back.isBeingClicked(ui) == True:
            ui = ui.HUB
          #  return (self.player.getAbilityList())
        elif self.item_equipped1.isBeingClicked(ui) == True:
            self.player.setAbilityIndex(0)
            # self.player.setCounter(0)
        elif self.item_equipped2.isBeingClicked(ui) == True:
            self.player.setAbilityIndex(1)
            # self.player.setCounter(1)
        elif self.item_equipped3.isBeingClicked(ui) == True:
            self.player.setAbilityIndex(2)
            # self.player.setCounter(2)
        elif self.item_equipped4.isBeingClicked(ui) == True:
            self.player.setAbilityIndex(3)
            # self.player.setCounter(3)
#        elif self.backButton.isBeingClicked(ui) == True:
#            ui = ui.HUB
            self.Shop.setCounter(1)
        elif self.item_equipped3.isBeingClicked(ui) == True:
            self.Shop.setAbilityIndex(2)
            self.Shop.setCounter(2)
        elif self.item_equipped4.isBeingClicked(ui) == True:
            self.Shop.setAbilityIndex(3)
            self.Shop.setCounter(3)
#        elif self.backButton.isBeingClicked(ui) == True:
#            ui = ui.HUB

        return ui
