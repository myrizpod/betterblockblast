class Tile:
    def __innit__(self,color,isempty):
        self.color = color
        self.isempty = isempty                   

class Grid:
    def __init__(self,size,tiles):
        self.size = size
        self.tiles = tiles

    def break_line(self,line):
        for i in range(self.size-1):
            self.tiles[line][i].isempty = True

    def break_col(self,col):
        for i in range(self.size-1):
            self.tiles[i][col].isempty = True

    def breaking(self):
        for i in range(self.size-1):
            can_break = True
            for j in range(self.size-1):
                if self.tiles[i][j].isempty == True:
                    can_break = False
            if can_break == True:
                self.break_line(i)
   
            can_break = True
            for j in range(self.size-1):
                if self.tiles[j][i].isempty == True:
                    can_break = False
            if can_break == True:
                self.break_col(i)        
    
    def can_place(self,object,place):
        for i in range(len(object.cubes)-1):
            x = object.cubes[i][0] + place[0]
            y = object.cubes[i][1] + place[1]
            if x < 0 or x > 7 or y < 0 or y > 7:
                return False
            if self.tiles[y][x].isempty == False:
                return False
        return True

    def place_object(self,object,place):
        if self.can_place(object,place) == False:
            return
        for i in range(len(object.cubes)-1):
            x = object.cubes[i][0] + place[0]
            y = object.cubes[i][1] + place[1]
            self.tiles[y][x].isempty = False



        
