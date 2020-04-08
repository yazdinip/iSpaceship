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
    def __init__(self, display, Shop):
        Screen.__init__(self, display)
        #self.Item = Item 
        self.Shop = Shop 
        self.init()
        
    
    
    def init(self):
         
        # Create the components of the main screen

        self.wallet = Text(f"You have ${self.Shop.getCurrency()}!" , 400, 50, WHITE, "Arial", 25)
        self.item_name = Text("Name: " + self.Shop.getCurrentA().getAbilityName(), 100, 100, WHITE, "Arial", 20)
        self.item_price = Text("Price: " + str(self.Shop.getCurrentA().getPrice())+"$", 100, 130, WHITE, "Arial", 20)
        self.item_damage = Text("Damage: " + str(self.Shop.getCurrentA().getAbilityDamage()), 100, 160, WHITE, "Arial", 20)
        
        self.item_cool_down = Text("Cool Down: " + str(self.Shop.getCurrentA().getCoolDown())+"s", 100, 190, WHITE, "Arial", 20)
        self.item_hit_chance = Text("Hit Chance: " + str(self.Shop.getCurrentA().getHitChance()*10)+"%", 100, 220, WHITE, "Arial", 20)
        
        #Buy: Section
        self.prev_buy = Button("Previous Item", 400, 100, 150, 50)
        self.next_buy = Button("Next Item", 600, 100, 100, 50)
        self.buy = Button("Buy Item", 500, 200, 100, 50)

        #Bought: Section
        self.item_bought_name = Text("Name: " + self.Shop.getCurrentB().getAbilityName(), 100, 300, WHITE, "Arial", 20)
        self.item_bought_price = Text("Price: " + str(self.Shop.getCurrentB().getPrice())+"$", 100, 330, WHITE, "Arial", 20)
        self.item_bought_damage = Text("Damage: " + str(self.Shop.getCurrentB().getAbilityDamage()), 100, 360, WHITE, "Arial", 20)
        self.item_bought_cool_down = Text("Cool Down: " + str(self.Shop.getCurrentB().getCoolDown())+"s", 100, 390, WHITE, "Arial", 20)
        self.item_bought_hit_chance = Text("Hit Chance: " + str(self.Shop.getCurrentB().getHitChance()*10)+"%", 100, 420, WHITE, "Arial", 20)

        self.prev_bought = Button("Previous Item", 400, 330, 150, 50)
        self.next_bought = Button("Next Item", 600, 330, 100, 50)
        self.swap = Button("Swap Item",500 , 400, 100, 50)

        #Abilities Section
        self.item_equipped1 = Button(self.Shop.getAbilityList()[0].getAbilityName(),100 , 510, 80, 60)
        self.item_equipped2 = Button(self.Shop.getAbilityList()[1].getAbilityName(),200 , 510, 80, 60)
        self.item_equipped3 = Button(self.Shop.getAbilityList()[2].getAbilityName(),300 , 510, 80, 60)
        self.item_equipped4 = Button(self.Shop.getAbilityList()[3].getAbilityName(),400 , 510, 80, 60)

        self.item_details = Text(f"Ability Details for {self.Shop.getAbilityList()[self.Shop.getAbilityIndex()].getAbilityName()} ", 500, 510, WHITE, "Arial", 15)
        self.item_equipped_price = Text("Price: " + str(self.Shop.getAbilityList()[self.Shop.getAbilityIndex()].getPrice())+"$", 600, 525, WHITE, "Arial", 12)
        self.item_equipped_damage = Text("Damage: " + str(self.Shop.getAbilityList()[self.Shop.getCounter()].getAbilityDamage()), 600, 540, WHITE, "Arial", 12)
        self.item_equipped_cool_down = Text("Cool Down: " + str(self.Shop.getAbilityList()[self.Shop.getCounter()].getCoolDown())+"s", 600, 555, WHITE, "Arial", 12)
        self.item_equipped_hit_chance = Text("Hit Chance: " + str(self.Shop.getAbilityList()[self.Shop.getCounter()].getHitChance()*10)+"%", 600, 570, WHITE, "Arial", 12)


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
            self.Shop.prevA()
        elif self.next_buy.isBeingClicked(ui) == True:
            self.Shop.nextA()
            #self.ShopUI.init()
#            print(self.Shop.getCurrentA().getAbilityName())
#            pygame.display.update()
#            self.item_name = Text("Name: " + self.Shop.getCurrentA().getAbilityName(), 100, 100, WHITE, "Arial", 20)
            #i = ui.SHOP
        elif self.next_bought.isBeingClicked(ui) == True:
            self.Shop.nextB()
        elif self.prev_bought.isBeingClicked(ui) == True:
            self.Shop.prevB()
        elif self.buy.isBeingClicked(ui) == True:
            self.Shop.buy()
        elif self.swap.isBeingClicked(ui) == True:
            self.Shop.equip()
        elif self.back.isBeingClicked(ui) == True:
            ui = ui.HUB
            return (self.Shop.getAbilityList())
        elif self.item_equipped1.isBeingClicked(ui) == True:
            self.Shop.setAbilityIndex(0)
            self.Shop.setCounter(0)
        elif self.item_equipped2.isBeingClicked(ui) == True:
            self.Shop.setAbilityIndex(1)
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
