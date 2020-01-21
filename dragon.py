from objects import objects
from random import randint
class dragon(objects):
    def __init__(self,height):
        self._shape = [[" "," "," "," "," "," "," "," ","(",",",",","(",","," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," ","(",",","'"," "," "," "," "," ","`","/"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" ",","," "," ",",","'"," "," ",",","-","-","."," "," ","`",","," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," ","`","{","D",","," ","{"," "," "," "," ","\\"," "," ",":"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," ","V",",",",","'"," "," "," "," ","/"," "," ","/"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," ","j",";",";"," "," "," "," ","/"," "," ",",","'"," ",",","-","-","-","."," "," "," "," ",",","-","-","-","."," "," "," "," "," "," ",","],[" "," "," "," ","\\",";","'"," "," "," ","/"," "," ",",","'"," ","/"," "," ","_"," "," ","\\"," "," ","/"," "," ","_"," "," ","\\"," "," "," ",",","'","/"],[" "," "," "," "," "," "," "," "," "," ","\\"," "," "," ","`","'"," "," ","/"," ","\\"," "," ","`","'"," "," ","/"," ","\\"," "," ","`",".","'"," ","/"," "],[" "," "," "," "," "," "," "," "," "," "," ","`",".","_","_","_",",","'"," "," "," ","`",".","_","_",",","'"," "," "," ","`",".","_","_",",","'"," "," "]]
        self._xcoordinate = 60
        self._ycoordinate = 12
        self._xsize = 38
        self._ysize = 9
        self._ylimit = [4,height-12]

    def CheckBoundary(self):
        if self._ycoordinate < self._ylimit[0]:
            self._ycoordinate = self._ylimit[0]
        elif self._ycoordinate > self._ylimit[1]:
            self._ycoordinate = self._ylimit[1]

    def MoveDrag(self,mandalorian):
        if self._ycoordinate > mandalorian.GetPos()[0]:
            self.moveUp()
        if self._ycoordinate < mandalorian.GetPos()[0]:
            self.moveDown()
        self.CheckBoundary()

    def moveUp(self):
        self._ycoordinate = self._ycoordinate - 1

    def moveDown(self):
        self._ycoordinate = self._ycoordinate + 1

class bulletd(objects):
    def __init__(self,Mandalorian):
        self._shape = [["\u001b[31m" + "\u25EF" + "\u001b[0m"]]
        y = randint(0,8)
        self._xcoordinate = Mandalorian.GetPos()[1]
        self._ycoordinate = Mandalorian.GetPos()[0] + y
        self._xsize = 1
        self._ysize = 1






 #        (,,(,
 #     (,'     `/
 # ,  ,'  ,--.  `,
 #  `{D, {    \  :
 #    V,,'    /  /
 #    j;;    /  ,' ,---.    ,---.      ,
 #    \;'   /  ,' /  _  \  /  _  \   ,'/
 #          \   `'  / \  `'  / \  `.' /
 #           `.___,'   `.__,'   `.__,'           ]
