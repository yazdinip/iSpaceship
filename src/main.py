import pygame
from res import *
from loadprofile import LoadProfile
from hub import Hub
from battleScreen import BattleScreen

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

    # Create screen
    loadUI = LoadProfile(display)
    hubUI = Hub(display)
    # shopUI = Shop(display, ... )
    battleUI = battleScreen(display)


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
                # elif ui == ui.SHOP:
                #     ui = shopScreen.checkForComponentClicks(ui)
                # elif ui == ui.BATTLE:
                #     ui = battleUI.checkForComponentClicks(ui)

            if event.type == pygame.QUIT:
                running = False
        
        # Clears display
        display.fill(BLACK)

        # Draw the space background
        background = pygame.image.load('img/background.png')
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
            pass

        pygame.display.update()

if __name__ == '__main__':
    main()