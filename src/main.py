import pygame
from res import *
from loadprofile import LoadProfile
from hub import Hub
from battleScreen import BattleScreen
from Spaceship import Spaceship
from player import Player

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
    # player1 = Player()
    # saveToFile(player1, Profile.PROFILE_1)
    # saveToFile(player1, Profile.PROFILE_2)
    # saveToFile(player1, Profile.PROFILE_3)
    # saveToFile(player1, Profile.PROFILE_4)

    # Create screen

    # shopUI = Shop(display, ... )

    list1, list2 = getTestList()
    # playerShip = loadFromFile(profile)
    aiShip = Spaceship(50,5,list2)

    player = loadFromFile(profile)
    battleUI = BattleScreen(display, aiShip, player, ui)
    hubUI = Hub(display, battleUI)
    loadUI = LoadProfile(display, hubUI)

    # Game loop
    while running:
        # deltaTime = clock.tick()

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ui == ui.LOAD_PROFILE:
                    ui = loadUI.checkForComponentClicks(ui)
                    hubUI.updateProfile(profile)
                elif ui == ui.HUB:
                    ui = hubUI.checkForComponentClicks(ui)
                # elif ui == ui.SHOP:
                #     ui = shopScreen.checkForComponentClicks(ui)
                elif ui == ui.BATTLE:
                    ui = battleUI.checkForComponentClicks(ui)

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
        # elif ui == ui.SHOP:
        #     shopScreen.update(deltaTime)
        #     shopScreen.draw()
        elif ui == ui.BATTLE:
        #     shopScreen.update(deltaTime)
            battleUI.draw()
            battleUI.drawComponents()
            

        pygame.display.update()

if __name__ == '__main__':
    main()
