from res import *
import pygbutton
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
    def __init__(self, display, Shop):
        Screen.__init__(self, display)
        #self.Item = Item 
        self.Shop = Shop 
        self.init()
    
    
    def init(self):
         
        # Create the components of the main screen
        print(self.Shop.check()) 

        self.item_name = Text("Name: " + self.Shop.currentDisplayedAItem.getAbilityName(), 100, 100, WHITE, "Arial", 20)
        self.item_price = Text("Price: " + str(abilityListA[0].getPrice())+"$", 100, 130, WHITE, "Arial", 20)
        self.item_damage = Text("Damage: " + str(abilityListA[0].getAbilityDamage()), 100, 160, WHITE, "Arial", 20)
        
        self.item_cool_down = Text("Cool Down: " + str(abilityListA[0].getCoolDown())+"s", 100, 190, WHITE, "Arial", 20)
        self.item_hit_chance = Text("Hit Chance: " + str(abilityListA[0].getHitChance()*10)+"%", 100, 220, WHITE, "Arial", 20)
        
        #Buy: Section
        self.prev_buy = Button("Previous Item", 400, 100, 150, 50)
        self.next_buy = Button("Next Item", 600, 100, 100, 50)
        self.buy = Button("Buy Item", 500, 200, 100, 50)

        #Bought: Section
        self.item_bought_name = Text("Name: " + abilityListB[0].getAbilityName(), 100, 300, WHITE, "Arial", 20)
        self.item_bought_price = Text("Price: " + str(abilityListB[0].getPrice())+"$", 100, 330, WHITE, "Arial", 20)
        self.item_bought_damage = Text("Damage: " + str(abilityListB[0].getAbilityDamage()), 100, 360, WHITE, "Arial", 20)
        self.item_bought_cool_down = Text("Cool Down: " + str(abilityListB[0].getCoolDown())+"s", 100, 390, WHITE, "Arial", 20)
        self.item_bought_hit_chance = Text("Hit Chance: " + str(abilityListB[0].getHitChance()*10)+"%", 100, 420, WHITE, "Arial", 20)

        self.prev_bought = Button("Previous Item", 400, 330, 150, 50)
        self.next_bought = Button("Next Item", 600, 330, 100, 50)
        self.swap = Button("Swap Item",500 , 400, 100, 50)
        
        #Abilities Section
        self.item_equipped1 = Button(abilityList[0].getAbilityName(),100 , 510, 80, 60)
        self.item_equipped2 = Button(abilityList[1].getAbilityName(),200 , 510, 80, 60)
        self.item_equipped3 = Button(abilityList[2].getAbilityName(),300 , 510, 80, 60)
        self.item_equipped4 = Button(abilityList[3].getAbilityName(),400 , 510, 80, 60)
        #self.item_bought_name = Text("Name: " + abilityList[0].getAbilityName(), 100, 300, WHITE, "Arial", 20)
        self.item_details = Text("Ability Details:", 500, 510, WHITE, "Arial", 15)
        self.item_equipped_price = Text("Price: " + str(abilityList[0].getPrice())+"$", 600, 525, WHITE, "Arial", 12)
        self.item_equipped_damage = Text("Damage: " + str(abilityList[0].getAbilityDamage()), 600, 540, WHITE, "Arial", 12)
        self.item_equipped_cool_down = Text("Cool Down: " + str(abilityList[0].getCoolDown())+"s", 600, 555, WHITE, "Arial", 12)
        self.item_equipped_hit_chance = Text("Hit Chance: " + str(abilityList[0].getHitChance()*10)+"%", 600, 570, WHITE, "Arial", 12)
        
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
            ui = ui.SHOP
        elif self.next_buy.isBeingClicked(ui) == True:
            
            print("next item") 
            ui = ui.SHOP
        elif self.next_bought.isBeingClicked(ui) == True:
            ui = ui.SHOP
        elif self.prev_bought.isBeingClicked(ui) == True:
            ui = ui.SHOP
        elif self.buy.isBeingClicked(ui) == True:
            ui = ui.SHOP
        elif self.swap.isBeingClicked(ui) == True:
            ui = ui.SHOP
        elif self.back.isBeingClicked(ui) == True:
            ui = ui.HUB
        elif self.item_equipped1.isBeingClicked(ui) == True:
            ui = ui.SHOP
        elif self.item_equipped2.isBeingClicked(ui) == True:
            ui = ui.SHOP
        elif self.item_equipped3.isBeingClicked(ui) == True:
            ui = ui.SHOP
        elif self.item_equipped4.isBeingClicked(ui) == True:
            ui = ui.SHOP
#        elif self.backButton.isBeingClicked(ui) == True:
#            ui = ui.HUB

        return ui
