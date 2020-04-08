from res import *

class LoadProfile(Screen):
    def __init__(self, display, hubUI):
        Screen.__init__(self, display)

        self.hubUI = hubUI
        self.init()
    
    def init(self):

        self.text = Text("Load Profile", 300, 100, WHITE, "Arial", 50)

        # Create the components of the main screen
        self.profile1 = Button("Profile 1", 350, 300, 100, 50)
        self.profile2 = Button("Profile 2", 350, 375, 100, 50)
        self.profile3 = Button("Profile 3", 350, 450, 100, 50)
        self.profile4 = Button("Profile 4", 350, 525, 100, 50)
        self.exit = Button("Exit", 200, 525, 100, 50)

        # Add components to components list
        self.components.append(self.profile1)
        self.components.append(self.profile2)
        self.components.append(self.profile3)
        self.components.append(self.profile4)
        self.components.append(self.exit)
        self.components.append(self.text)



    
    def checkForComponentClicks(self, ui, profile):
        if self.profile1.isBeingClicked(ui) == True:
            ui = ui.HUB
            profile = Profile.PROFILE_1

        if self.profile2.isBeingClicked(ui) == True:
            ui = ui.HUB
            profile = Profile.PROFILE_2
        if self.profile3.isBeingClicked(ui) == True:
            ui = ui.HUB
            profile = Profile.PROFILE_3

        if self.profile4.isBeingClicked(ui) == True:
            ui = ui.HUB
            profile = Profile.PROFILE_4

        if self.exit.isBeingClicked(ui) == True:
            raise SystemExit

        return ui, profile