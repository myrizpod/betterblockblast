from Cube import Cube
from Grid import Grid
from Object import Object

import random




ALL_OBJECTS =[ Object([Cube(0,0,0),Cube(0,0,1)]),
               Object([Cube(0,0,0),Cube(0,0,1),Cube(0,0,-1)]),
               Object([Cube(0,0,0),Cube(0,0,1),Cube(0,0,-1),Cube(0,0,2)]),
               Object([Cube(0,0,0),Cube(0,0,1),Cube(0,0,-1),Cube(0,0,2),Cube(0,0,-2)]),
               Object([Cube(0,0,0),Cube(0,1,-1),Cube(0,-1,1)]),
               Object([Cube(0,0,0),Cube(0,0,1),Cube(0,0,-1),Cube(0,1,-1)]),
               Object([Cube(0,0,0),Cube(0,0,0),Cube(0,0,0),Cube(0,0,0),Cube(0,0,0),Cube(0,0,0),Cube(0,0,0),Cube(0,0,0),Cube(0,0,0)]),
               Object([Cube(0,1,1),Cube(0,1,0),Cube(0,1,-1),Cube(0,0,-1),Cube(0,-1,-1)]),
               Object([Cube(0,0,0),Cube(0,0,-1),Cube(0,-1,0)]),
               Object([Cube(0,0,0),Cube(0,1,0),Cube(0,0,1),Cube(0,0,-1)]),
               Object([Cube(0,0,0),Cube(0,0,1),Cube(0,1,1),Cube(0,1,0),Cube(0,1,-1),Cube(0,0,-1)]),
               Object([Cube(0,0,0),Cube(0,0,-1),Cube(0,1,0),Cube(0,1,1)]),
               Object([Cube(0,0,0),Cube(0,1,0),Cube(0,0,1),Cube(0,1,1)]),
               Object([Cube(0,0,0)])

]




def give_objects(grid):
    objects = []
    for i in range(3):
        obj = ALL_OBJECTS[random.randint(0,len(ALL_OBJECTS)-1)]
        for i in range(random.randint(0,3)):
            obj.rotate()
        if  random.randint(0,1) == 1:
            obj.mirrorX()
        obj.setColor(random.randint(0,9))    
        objects.append(obj)
    return objects

