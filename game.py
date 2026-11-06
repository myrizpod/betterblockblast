import random

import pygame

from Cube import Cube
from Grid import Grid
from Object import Object
from garbage import particles



class Game:
    def __init__(self,grid,m):
        self.grid = grid
        self.grid.parent = self
        self.particles = []
        self.score = 0
        self.streak = 40
        self.screenMult = m
        self.givenTiles = []
        self.font = pygame.font.Font("assets/fonts/m6x11.ttf",16)

    def outlinedText(self,buffer,text,pos):
        for x in range(-1,2):
            for y in range(-1,2):
                surf =self.font.render(text, False, (0, 0, 0))
                buffer.blit(surf, (pos[0]+x-surf.width/2,pos[1]+y-surf.height/2))
        surf = self.font.render(text, False, (255, 255, 255))
        buffer.blit(surf, (pos[0]-surf.width/2,pos[1]-surf.height/2))
        return surf.get_rect()


    def draw(self,buffer):
        buffer.fill((0,0,0))
        self.grid.draw(buffer)

        for p in self.particles:
            p.draw(buffer)

        self.outlinedText(buffer,str(self.score),(30,70))

        self.outlinedText(buffer,'X'+str(self.streak),(30,50))


        if self.streak>1:
            self.particles.append(particles.Flame(pygame.Vector2(30, 50), self.streak))





    def update(self):
        gpos = pygame.mouse.get_pos()
        gpos = (gpos[0]//16//self.screenMult-4,gpos[1]//16//self.screenMult-4)
        self.grid.place_object(Object([Cube(random.randint(0,9),0,0)]),gpos)
        self.grid.update()

        for p in reversed(self.particles):
            if p.update():
                self.particles.remove(p)

    def breakAnim(self,x,y,col):
        for _ in range(20):
             self.particles.append(particles.Break(pygame.Vector2(x, y), col))

    def lineBreakPts(self):
        self.score+=10*self.streak