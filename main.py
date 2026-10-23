"""The game's main file"""

# Library import

import pygame
import constants as ct
import game

class App:

    def __init__(self, test = False):
        """
        Called on game startup, all basic stuff
        """

        #Creating basics of the game

        self.test = test
        self.screen_mult = 3
        ct.SCREEN_MULT = self.screen_mult
        self.screen_size = (ct.GAME_DRAW_SIZE_X * self.screen_mult, ct.GAME_DRAW_SIZE_Y * self.screen_mult) #if test else (ct.GAME_DRAW_SIZE_X, ct.GAME_DRAW_SIZE_Y)
        pygame.init()
        pygame.mixer.init()
        self.running = True
        ct.RENDER_BUFFER = pygame.Surface((ct.GAME_DRAW_SIZE_X, ct.GAME_DRAW_SIZE_Y), pygame.OPENGL)
        ct.CLOCK = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Block Blast')
        icon = pygame.image.load("assets/images/icon.png")
        pygame.display.set_icon(icon)

        self.game = game.Game()

        #Starting game loop
        self.loop()
        pygame.quit()

    def loop(self):
        """
        Global game loop
        """

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.running = False
            ct.CLOCK.tick(30)
            ct.RENDER_BUFFER.fill((0,255,0))
            self.update()
            self.draw()
            pygame.display.update()

        pygame.quit()


    def update(self):
        self.game.update()

    def draw(self):
        self.game.draw()
        if self.test:
            pygame.transform.scale_by(ct.RENDER_BUFFER, self.screen_mult, self.screen)
        else:
            self.screen.blit(ct.RENDER_BUFFER, (0, 0))
        pygame.display.update()



if __name__ == '__main__':
    App(True)
