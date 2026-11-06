import random

import pygame
from psycopg.types import none

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
        self.streak = 1
        self.screenMult = m
        self.heldObject = None
        self.keepStreak = False
        self.givenObjects = algo.give_objects(self.grid)
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


        self.draw_given_objects(buffer,self.givenObjects)
        self.drawHeldOBject(buffer)


    def draw_given_objects(self, buffer,objects): 
        for k in range(3):
            drawn_object = objects[k]
            if drawn_object!=None:
                for i in drawn_object.cubes:
                    buffer.blit(Grid.coloredTiles, (56 + 96*k + 16*i.X, 200 + 16*i.Y, 16, 16), (16*i.color,0,16,16))

    def drawHeldOBject(self,buffer):
        if self.heldObject!=None:
            mpos = pygame.mouse.get_pos()
            mpos = (mpos[0] // self.screenMult, mpos[1] // self.screenMult)
            for i in self.heldObject.cubes:
                buffer.blit(Grid.coloredTiles, (mpos[0] -8  + 16 * i.X, mpos[1] -8 + 16 * i.Y, 16, 16), (16 * i.color, 0, 16, 16))


    def update(self):
        mpos = pygame.mouse.get_pos()
        mpos = (mpos[0]//16//self.screenMult,mpos[1]//16//self.screenMult)
        self.grid.update()

        if self.heldObject==None and self.givenObjects==[None,None,None]:
            self.givenObjects = algo.give_objects(self.grid)
            if not self.keepStreak:
                self.streak =1
            self.keepStreak =False


        if self.streak>1:
            self.particles.append(particles.Flame(pygame.Vector2(30, 50), self.streak))

        if pygame.mouse.get_just_pressed()[0]:
            self.mousePressEvent(mpos)

        for p in reversed(self.particles):
            if p.update():
                self.particles.remove(p)

    def breakAnim(self,x,y,col):
        for _ in range(20):
             self.particles.append(particles.Break(pygame.Vector2(x, y), col))

    def lineBreakPts(self):
        self.score+=10*self.streak
        self.streak+=1
        self.keepStreak = True

    def mousePressEvent(self,mpos):
        for i in range(3):
            if pygame.Rect((1 + 6*i, 11, 6, 6)).collidepoint(mpos):
                self.heldObject,self.givenObjects[i] =self.givenObjects[i],self.heldObject
                break
        gpos = (mpos[0] - self.grid.origin[0] // 16, mpos[1] - self.grid.origin[1] // 16)
        if gpos[0]<0 or gpos[1]<0 or gpos[0]>self.grid.size or gpos[1]>self.grid.size or self.heldObject==None:
            return
        if self.grid.place_object(self.heldObject, gpos):
            self.heldObject=None