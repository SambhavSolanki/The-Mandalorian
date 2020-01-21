from objects import objects
from random import randint

class speed(objects):
    def __init__(self,yl):
        self._shape = [["\u231B"]]
        x = randint(-3,3)
        y = randint(4,yl)
        self._xcoordinate = 105 + x
        self._ycoordinate = y
        self._xsize = 1
        self._ysize = 1
