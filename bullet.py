from objects import objects

class bullet(objects):
    def __init__(self,Mandalorian):
        self._shape = [["\u001b[32m" + "\u2733" + "\u001b[0m"]]
        self._xcoordinate = Mandalorian.GetPos()[1]
        self._ycoordinate = Mandalorian.GetPos()[0]
        self._xsize = 1
        self._ysize = 1
