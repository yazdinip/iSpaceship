from enum import Enum
import pygame

# Global final constants available to all classes

# Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Positions
CENTER_SCREEN_X = SCREEN_WIDTH / 2
CENTER_SCREEN_Y = SCREEN_HEIGHT / 2

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class UI(Enum):
    LOAD_PROFILE = 1
    HUB = 2
    SHOP = 3
    BATTLE = 4

# class Profile(Enum):
#     PROFILE_1 = 1   # defult
#     PROFILE_2 = 2
#     PROFILE_3 = 3
#     PROFILE_4 = 4

class Screen:
    def __init__(self, display):
        self.display = display

         # List holds all the components of the screen (buttons, text, etc)
        self.components = []
    
    def draw(self):
        for component in self.components:
            component.draw(self.display)

class Text:
    def __init__(self, text, x, y, colour, font, fontSize):
        self.text = text
        self.x = x
        self.y = y
        self.colour = colour
        self.font = font
        self.fontSize = fontSize
    
    def update(self, text):
        self.text = text
    
    # Draws text that never changes once it is displayed on display
    def draw(self, display):
        font = pygame.font.SysFont(self.font, self.fontSize)
        text = font.render(self.text, True, self.colour, None)
        display.blit(text, (self.x, self.y))
    
    def getText(self):
        return self.text

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = Text(text, x,  y, BLACK, "Arial", 20)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, display):
        pygame.draw.rect(display, WHITE, (self.x, self.y, self.width, self.height))
        self.text.draw(display)
    
    def isBeingClicked(self, state):
        mouse = pygame.mouse.get_pos()
        
        if self.isClickInTheButton(mouse[0], mouse[1]):
            return True
        
        return state
    
    def isClickInTheButton(self, mouseX, mouseY):
        if self.x < mouseX < self.x + self.width:
            if self.y < mouseY < self.y + self.height:
                return True
        
        return False