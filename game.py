import pygame

class Game:
    def __init__(self,grid):
        self.tile = pygame.image.load("assets/images/empty_tile.png")
        self.tilerect = self.tile.get_rect()
        self.grid = grid

    def draw(self,buffer):
        buffer.fill((255,255,255))
        for i in range(self.grid.size):
            for j in range(self.grid.size):
                buffer.blit(self.tile,(64+16*i,64+16*j,16,16))


    def update(self):
        pass