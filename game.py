import random

import pygame

from Cube import Cube
from Grid import Grid
from Object import Object
from garbage import particles
import algo

class Game:
    def __init__(self,grid,m):
        self.grid = grid
        self.grid.parent = self
        self.particles = []
        self.score = 0
        self.screenMult = m
        self.givenObjects = algo.give_objects(self.grid)

    def draw(self,buffer):
        buffer.fill((0,0,0))
        self.grid.draw(buffer)
        self.draw_given_objects(buffer,self.givenObjects)

        # self.particles.append(particles.Flame(pygame.Vector2(200,100),int(fah)))
        # fah = max(min(7,fah),0)
        # if pygame.mouse.get_just_pressed()[0]:
        #     for _ in range(20):
        #         self.particles.append(particles.Break(pygame.Vector2(100, 100), int(fah)))



        for p in self.particles:
            p.draw(buffer)
    def draw_given_objects(self, buffer,objects): 
        for k in range(3):
            drawn_object = objects[k]
            for i in drawn_object.cubes:
                buffer.blit(Grid.coloredTiles, (64 + 64*k + 16*i.X, 192 + 16*i.Y, 16, 16), (16*i.color,0,16,16))


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
        self.score+=100