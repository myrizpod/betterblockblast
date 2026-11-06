class Object:
    def __init__(self, cubes):
          self.cubes = cubes

    def rotate(self):
        for i in self.cubes:
            i[0] = i[1]
            i[1] = -i[0] 

    def mirrorX(self):
        for i in self.cubes:
            i[0] = -i[0]                 