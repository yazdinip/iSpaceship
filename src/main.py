import pygame
from res import *
from loadprofile import LoadProfile
from hub import Hub
from battleScreen import BattleScreen
from Spaceship import Spaceship
from player import Player
from Shop import Shop
from ShopUI import ShopUI

import Story

def main():
    global running, display

    # Initialize pygame
    pygame.init()
    display = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("iSpaceship")
    # clock = pygame.time.Clock()

    running = True
    ui = UI.LOAD_PROFILE
    profile = Profile.PROFILE_1

    ##  Uncomment to generate new profile data
    player1 = Player()
    saveToFile(player1, Profile.PROFILE_1)
    saveToFile(player1, Profile.PROFILE_2)
    saveToFile(player1, Profile.PROFILE_3)
    saveToFile(player1, Profile.PROFILE_4)

    # Create screen

    # shopUI = Shop(display, ... )

    list1, list2 = getTestList()
    # playerShip = loadFromFile(profile)
    aiShip = Spaceship(50,5,list2)

    player = loadFromFile(profile)
    battleUI = BattleScreen(display, Story.enemy1, player, ui)
    hubUI = Hub(display, battleUI, player)
    loadUI = LoadProfile(display, hubUI)
    
    abilityListA = Story.abilityA
    abilityListB = Story.abilityB
    abilityList = player.abilityList
    currency = player.getCurrency()
    
    shopUI = ShopUI(display, player)

    beginButton = Button("Begin Battle", 650, 100, 100, 50) # For making a new battle
    textMoney = Text("Currency: " + str(player.getCurrency()), 350, 475, WHITE, "Arial", 30)
    textMission = Text("Current Mission: " + str(player.getMissionNum()), 350, 510, WHITE, "Arial", 30)
    playerSpaceship = player.getSpaceShip()
    enemySpaceship = aiShip
    
    # Game loop
    while running:
        # deltaTime = clock.tick()

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ui == ui.LOAD_PROFILE:
                    ui, profile = loadUI.checkForComponentClicks(ui, profile)
                    hubUI.updateProfile(profile)
                elif ui == ui.HUB:
                    ui = hubUI.checkForComponentClicks(ui)
                    hubUI.init()
                    #print("hello")
                elif ui == ui.SHOP:
                    ui = shopUI.checkForComponentClicks(ui)
                    shopUI.init()
                     
                    textMoney = Text("Currency: " + str(player.getCurrency()), 350, 475, WHITE, "Arial", 30)
                    textMission = Text("Current Mission: " + str(player.getMissionNum()), 350, 510, WHITE, "Arial", 30)
                elif ui == ui.BATTLE:
                    ui = battleUI.checkForComponentClicks(ui)

                    if beginButton.isBeingClicked(ui) == True:
                        player.resetHealth()
                        result = battleUI.newBattle(enemySpaceship, player)
                        if result == True:
                            # self.victoryString = "Victory!"
                            player.setMissionNum()
                            player.addCurrency(1000)

                            
                        elif result == False:
                            # self.victoryString = "Humiliation!"
                            player.resetMissionNum()
                            player.removeCurrency(500)
                            
                        # self.drawComponents()
                        print("battle result = " + str(result))
                        if(player.getMissionNum() == 0):
                            battleUI = BattleScreen(display, Story.enemy1, player, ui)
                        elif(player.getMissionNum() == 1):
                            battleUI = BattleScreen(display, Story.enemy2, player, ui)
                        elif(player.getMissionNum() == 2):
                            battleUI = BattleScreen(display, Story.enemy3, player, ui)
                        elif(player.getMissionNum() == 3):
                            battleUI = BattleScreen(display, Story.enemy3, player, ui)

                        #battleUI = BattleScreen(display, aiShip, player, ui)
                        textMoney = Text("Currency: " + str(player.getCurrency()), 350, 475, WHITE, "Arial", 30)
                        textMission = Text("Current Mission: " + str(player.getMissionNum()), 350, 510, WHITE, "Arial", 30)

                        

            if event.type == pygame.QUIT:
                running = False
        
        # Clears display
        display.fill(BLACK)
        # Draw the space background
        background = pygame.image.load('assets/img/background.png')
        display.blit(background, (0, 0))
        
        if ui == ui.LOAD_PROFILE:
            loadUI.draw()
        elif ui == ui.HUB:
            hubUI.draw()
            hubUI.components.append(textMoney)
            hubUI.components.append(textMission)
        elif ui == ui.SHOP:
            display.fill(BLACK)
        # Draw the space background
            background = pygame.image.load('assets/img/background_shop.png')
            display.blit(background, (0, 0))
            shopUI.draw()
            #shopScreen.update(deltaTime)
           # shopUI.init()
        elif ui == ui.BATTLE:
            battleUI.draw()
            battleUI.drawComponents()
            battleUI.components.append(beginButton)

            

        pygame.display.update()

if __name__ == '__main__':
    main()
