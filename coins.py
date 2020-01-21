from objects import objects
from random import randint
class coins(objects):
    def __init__(self,yl):
        self._shape = [["\u001b[33m" + "\u2A37" + "\u001b[0m"]]
        x = randint(-3,3)
        y = randint(4,yl)
        self._xcoordinate = 105 + x
        self._ycoordinate = y
        self._xsize = 1
        self._ysize = 1
