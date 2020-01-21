from extraFunctions import *
class objects:
    def __init__(self):
        self._xcoordinate = None
        self._ycoordinate = None
        self._xsize = None
        self._ysize = None
        self._shape = None
        # self._fore = None
        # self._back = None


    #1 Black: \u001b[30m
    #2 Red: \u001b[31m
    #3 Green: \u001b[32m
    #4 Yellow: \u001b[33m
    #5 Blue: \u001b[34m
    #6 Magenta: \u001b[35m
    #7 Cyan: \u001b[36m
    #8 White: \u001b[37m
    #
    # Reset: \u001b[0m
    def GetPos(self):
        return [self._ycoordinate,self._xcoordinate]

    def GetLimit(self):
        return [self._ysize,self._xsize]

    def AddObject(self,grid):
        for i in range(self._ysize):
            for j in range(self._xsize):
                grid.AddToGrid(self.GetPos()[0]+i,self.GetPos()[1]+j,self._shape[i][j])

    def MoveLeft(self):
        self._xcoordinate = self.GetPos()[1] - 1

    def MoveRight(self):
        self._xcoordinate = self.GetPos()[1] + 1


    def Overlap(self,obj2):
        if obj2.GetPos()[1] + obj2.GetLimit()[1] >= self.GetPos()[1] and obj2.GetPos()[1] < self.GetPos()[1] + self.GetLimit()[1]:
            if obj2.GetPos()[0] + obj2.GetLimit()[0] - 1 >= self.GetPos()[0] and obj2.GetPos()[0] < self.GetPos()[0] + self.GetLimit()[0]:
                return True
            else:
                return False
        else:
            return False
