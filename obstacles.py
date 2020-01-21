from objects import objects
from random import randint
class obstaclesH(objects):
    def __init__(self,yl):
        self._shape = [["\u001b[34m" + "\u2550","\u001b[34m" + "\u2550","\u001b[31m" + "\u2550","\u001b[31m" + "\u2550","\u001b[31m" + "\u2550","\u001b[31m" + "\u2550","\u001b[31m" + "\u2550","\u001b[31m" + "\u2550","\u001b[31m" + "\u2550","\u001b[31m" + "\u2550","\u001b[34m" + "\u2550","\u001b[34m" + "\u2550",]]
        x = randint(-3,3)
        y = randint(4,yl)
        self._xcoordinate = 104 + x
        self._ycoordinate = y
        self._xsize = 12
        self._ysize = 1

class obstaclesV(objects):
    def __init__(self,yl):
        self._shape = [["\u001b[34m" + "\u2551"],["\u001b[31m" + "\u2551"],["\u001b[31m" + "\u2551"],["\u001b[31m" + "\u2551"],["\u001b[31m" + "\u2551"],["\u001b[34m" + "\u2551"]]
        x = randint(-3,3)
        y = randint(4,yl-8)
        self._xcoordinate = 104 + x
        self._ycoordinate = y
        self._xsize = 1
        self._ysize = 6

class obstaclesD1(objects):
    def __init__(self,yl):
        self._shape = [["\033[1m" + "\u001b[34m" + "\u2572"," "," "," "," "],[" ","\033[1m" + "\u001b[31m" + "\u2572"," "," "," "],[" "," ","\033[1m" + "\u001b[31m" + "\u2572"," "," "],[" "," "," ","\033[1m" + "\u001b[31m" + "\u2572"," "],[" "," "," "," ","\033[1m" + "\u001b[34m" + "\u2572"]]
        x = randint(-3,3)
        y = randint(4,yl-8)
        self._xcoordinate = 104 + x
        self._ycoordinate = y
        self._xsize = 5
        self._ysize = 5

    def Overlap(self,obj2):
        flag = 0
        for i in range(self._ysize):
            if obj2.GetPos()[1] + obj2.GetLimit()[1] >= self.GetPos()[1] + i and obj2.GetPos()[1] <= self.GetPos()[1] + i:
                if obj2.GetPos()[0] + obj2.GetLimit()[0] >= self.GetPos()[0] + i and obj2.GetPos()[0] <= self.GetPos()[0] + i:
                    flag = 1
        if flag == 1:
            return True
        else:
            return False

class obstaclesD2(objects):
    def __init__(self,yl):
        self._shape = [[" "," "," "," ","\033[1m" + "\u001b[34m" + "\u2571"],[" "," "," ","\033[1m" + "\u001b[31m" + "\u2571"," "],[" "," ","\033[1m" + "\u001b[31m" + "\u2571"," "," "],[" ","\033[1m" + "\u001b[31m" + "\u2571"," "," "," "],["\u001b[34m" + "\u2571"," "," "," "," "]]
        x = randint(-3,3)
        y = randint(4,yl-8)
        self._xcoordinate = 104 + x
        self._ycoordinate = y
        self._xsize = 5
        self._ysize = 5

    def Overlap(self,obj2):
        flag = 0
        for i in range(self._ysize):
            if obj2.GetPos()[1] + obj2.GetLimit()[1] >= self.GetPos()[1] +self._ysize - i and obj2.GetPos()[1] < self.GetPos()[1] + self._ysize - i:
                if obj2.GetPos()[0] + obj2.GetLimit()[0] >= self.GetPos()[0] + i and obj2.GetPos()[0] < self.GetPos()[0] + i:
                    flag = 1
        if flag == 1:
            return True
        else:
            return False
