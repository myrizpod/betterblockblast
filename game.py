import pygame

from garbage import particles


class Game:
    def __init__(self):
        self.particles = []

    def draw(self,buffer):
        buffer.fill((0,0,0))

        fah = pygame.mouse.get_pos()[0]/30

        self.particles.append(particles.Flame(pygame.Vector2(200,100),int(fah)))

        fah = max(min(7,fah),0)

        if pygame.mouse.get_just_pressed()[0]:
            for _ in range(20):
                self.particles.append(particles.Break(pygame.Vector2(100, 100), int(fah)))



        for p in self.particles:
            p.draw(buffer)

    def update(self):
        for p in reversed(self.particles):
            if p.update():
                self.particles.remove(p)