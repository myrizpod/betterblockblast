import pygame
import game
import Grid as grid

BUFFER_SCALE_X = 320
BUFFER_SCALE_Y = 320

class App:

    def __init__(self,m):
        self.screen_mult = m
        self.screen_size = (BUFFER_SCALE_X * self.screen_mult, BUFFER_SCALE_Y * self.screen_mult)
        pygame.init()
        pygame.font.init()
        pygame.mixer.init() #sons (sert peut etre a rien)
        self.running = True
        self.buffer = pygame.Surface((BUFFER_SCALE_X, BUFFER_SCALE_Y), pygame.OPENGL)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Block Blast')
        icon = pygame.image.load("assets/images/icon.png")
        pygame.display.set_icon(icon)

        
        self.game = game.Game(grid.generateEmpty(8),m)
        self.loop()
        pygame.quit()

    def loop(self):
        while self.running:
            # a chier
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.running = False


            self.clock.tick(60)
            self.buffer.fill((0,255,0))
            self.update()
            self.draw()

        pygame.quit()


    def update(self):
        self.game.update()

    def draw(self):
        self.game.draw(self.buffer)
        pygame.transform.scale_by(self.buffer, self.screen_mult, self.screen)
        pygame.display.update()

if __name__ == '__main__':
    App(3)
