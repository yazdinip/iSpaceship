from res import *
import pygame

class Hub(Screen):
    def __init__(self, display, battleUI, player):
        Screen.__init__(self, display)

        self.battleUI = battleUI
        self.profile = Profile.PROFILE_1 # Defult value
        self.player = player
        self.init()
    
    def init(self):
        # Create the components of the main screen
        self.textWelcome = Text("Welcome to the Hub!", 200, 100, WHITE, "Arial", 50)
        self.textProfile = Text("Profile " + str(self.profile.value) + " selected.", 350, 200, WHITE, "Arial", 50)
        # self.textMoney = Text("Currency: " + str(self.player.getCurrency()), 350, 475, WHITE, "Arial", 30)
        # self.textMission = Text("Current Mission: " + str(self.player.getMissionNum()), 350, 510, WHITE, "Arial", 30)

        self.battle = Button("Battle", 200, 375, 100, 50)
        self.shop = Button("Shop", 550, 375, 100, 50)
        self.profiles = Button("New Profile", 200, 525, 100, 50)

        # Add components to components list
        self.components.clear()     # Clear components before drawing them
        self.components.append(self.battle)
        self.components.append(self.shop)
        self.components.append(self.profiles)

        self.components.append(self.textWelcome)
        self.components.append(self.textProfile)
        # self.components.append(self.textMoney)
        # self.components.append(self.textMission)
    
    def checkForComponentClicks(self, ui):
        if self.battle.isBeingClicked(ui) == True:
            ui = ui.BATTLE

        if self.shop.isBeingClicked(ui) == True:
            ui = ui.SHOP

        if self.profiles.isBeingClicked(ui) == True:
            ui = ui.LOAD_PROFILE

        return ui

    def updateProfile(self, profile):
        self.profile = profile
        self.player = loadFromFile(profile)
        self.battleUI.updatePlayer(self.player)
        self.init()
