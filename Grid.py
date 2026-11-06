import random
import pygame


class Tile:
    def __init__(self,color,isempty):
        self.color = color
        self.isempty = isempty


class Grid:
    emptyTile = pygame.image.load("assets/images/empty_tile.png")
    tileRect = emptyTile.get_rect()
    coloredTiles = pygame.image.load("assets/images/tiles.png")

    def __init__(self,size,tiles):
        self.size = size
        self.tiles = tiles
        self.parent = None


    def break_line(self,line):
        self.parent.lineBreakPts()
        for i in range(self.size):
            self.parent.breakAnim(72 + 16 * i, 72 + 16 * line,self.tiles[line][i].color)
            self.tiles[line][i].isempty = True

    def break_col(self,col):
        self.parent.lineBreakPts()
        for i in range(self.size):
            self.parent.breakAnim(72 + 16 * col, 72 + 16 * i, self.tiles[i][col].color)
            self.tiles[i][col].isempty = True

    def breaking(self):
        tilesData = [[self.tiles[j][i].isempty for i in range(self.size)] for j in range(self.size)]
        for i in range(self.size):
            can_break = True
            for j in range(self.size):
                if tilesData[i][j]:
                    can_break = False
            if can_break == True:
                self.break_line(i)
   
            can_break = True
            for j in range(self.size):
                if tilesData[j][i]:
                    can_break = False
            if can_break == True:
                self.break_col(i)        
    
    def can_place(self,object,place):
        for i in range(len(object.cubes)):
            x = object.cubes[i].X + place[0]
            y = object.cubes[i].Y + place[1]
            if x < 0 or x > 7 or y < 0 or y > 7:
                return False
            if self.tiles[y][x].isempty == False:
                return False
        return True

    def place_object(self,object,place):
        if not 0<=place[0]<self.size or not 0<=place[1]<self.size:
            print(place,self.size)
            return
        if self.can_place(object,place) == False:
            return
        for i in range(len(object.cubes)):
            x = object.cubes[i].X + place[0]
            y = object.cubes[i].Y + place[1]
            self.tiles[y][x].isempty = False
            self.tiles[y][x].color = object.cubes[i].color

    def draw(self, buffer):
        for i in range(self.size):
            for j in range(self.size):
                if self.tiles[j][i].isempty:
                    buffer.blit(Grid.emptyTile, (64 + 16 * i, 32 + 16 * j, 16, 16))
                else:
                    buffer.blit(Grid.coloredTiles, (64 + 16 * i, 32 + 16 * j, 16, 16), (16*self.tiles[j][i].color,0,16,16))


    def update(self):
        self.breaking()


def generateEmpty(size):
    return Grid(size,[[Tile(0,True) for _ in range(size)] for _ in range(size)])

def generateRandom(size):
    return Grid(size,[[Tile(random.randint(0,9),False) for _ in range(size)] for _ in range(size)])

        
