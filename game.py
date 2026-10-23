import constants as ct
import pygame

#States
MAIN_MENU = "mainmenu"
PAUSED = "paused"
INGAME = "ingame"

class Game:
    def __init__(self):
        self.state = MAIN_MENU

    def draw(self):
        ct.RENDER_BUFFER.fill((255,0,0))
        if self.state == MAIN_MENU:
            pass
        elif self.state == PAUSED:
            pass
        elif self.state == INGAME:
            pass


    def update(self):
        if self.state == MAIN_MENU:
            pass
        elif self.state == PAUSED:
            pass