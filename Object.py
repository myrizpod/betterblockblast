class Object:
    def __init__(self, cubes):
          self.cubes = cubes

    def rotate(self,cubes):
        for i in cubes:
            i.X,i.Y = i.Y,-i.X

    def mirrorX(self,cubes):
        for i in cubes:
            i.X = -i.X

    def setColor(self,col):
        for e in self.cubes:
            e.color = col
