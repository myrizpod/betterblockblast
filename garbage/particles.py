#COMPLETELY USELESS :D
import pygame
import random



class Particle:
    def __init__(self,pos,vel,acc=pygame.Vector2(0,0),fric=1.0,dur=0):
        self.pos = pos
        self.baseDur = dur
        self.vel = vel
        self.acc = acc
        self.exist = True
        self.fric = fric
        self.dur = dur


    def draw(self,buffer):
        pass

    def update(self):
        self.pos+=self.vel
        self.vel+=self.acc
        self.vel*=self.fric
        self.dur-=1
        if self.dur<=0:
            return True
        return False

def mix(c1,c2,f):
    rf = 1-f
    return (c1[0]*rf+c2[0]*f,c1[1]*rf+c2[1]*f,c1[2]*rf+c2[2]*f)


DCOL = ((212,30,60),(214,26,136),(120,215,255)) #Couleurs debut de flamme
MCOL = ((255,184,74),(255,122,125),(176,255,241)) #Couleurs milieu de flamme
LCOL = (250,255,255) #Couleur fin flamme


def getFlameCol(heat,adv):
    if heat<=10:
        dc = mix(DCOL[0],DCOL[1],heat/10)
        mc = mix(MCOL[0],MCOL[1],heat/10)
    else:
        dc = mix(DCOL[1],DCOL[2],heat/10-1)
        mc = mix(MCOL[1],MCOL[2],heat/10-1)
    if adv<=0.5:
        return mix(dc,mc,adv*2)
    else:
        return mix(mc, LCOL, adv * 2-1)

class Flame(Particle):

    def __init__(self,pos,heat):
        self.heat = min(heat,20)
        super().__init__(pos+pygame.Vector2(random.random()*4-2,random.random()*4-2),pygame.Vector2(random.random()-0.5,random.random()-2),pygame.Vector2(0,0),1,random.randint(45,75))

    def draw(self,buffer):
        pygame.draw.circle(buffer,getFlameCol(self.heat,max(self.dur/self.baseDur-0.3,0)),self.pos,self.dur/10)



class Break(Particle):
    def __init__(self,pos,col):
        tiles = pygame.image.load("assets/images/tiles.png")

        x = random.randint(0,15)+col*16
        y = random.randint(0,15)
        self.col = tiles.unmap_rgb(pygame.PixelArray(tiles)[x, y])
        self.size = random.random()*3
        super().__init__(pos+pygame.Vector2(random.random()*10-5,random.random()*10-5),pygame.Vector2(random.random()-0.5,-random.random()),pygame.Vector2(0,0.1),1,random.randint(15,35))

    def draw(self,buffer):
        pygame.draw.rect(buffer,self.col,(self.pos.x,self.pos.y,self.size,self.size))