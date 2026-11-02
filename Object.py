class Object:
    def __init__(self, cubes, rot):
          self.cubes = cubes

    def rotate(self,cubes):
        for i in cubes:
            i[0] = i[1]
            i[1] = -i[0] 

    def mirrorX(self,cubes):
        for i in cubes:
            i[0] = -i[0]                 