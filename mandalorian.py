from colorama import Fore, Back, Style , init
from extraFunctions import *
from math import floor
from objects import objects
class mandalorian(objects):

    def __init__(self,height,length):
        self._shape = [ [" ","0"," "," "," ","/"],["|","_","|","-","/"," "],["/","_","\\","_"," "," "]]
        self._xcoordinate = 1
        self._ycoordinate = height-6
        self._xsize = 6
        self._ysize = 3
        self.__yvel= 0
        self.__ylimit = [4,height-6]
        self.__xlimit = [1,length-8]

    def MoveMandalorian(self,command):
        if command is 'd':
            self.MoveMandalorianRight()
            self.MoveMandalorianDown()
        elif command is 'a':
            self.MoveMandalorianLeft()
            self.MoveMandalorianDown()
        elif command is 'w':
            self.MoveMandalorianUp()
        else:
            self.MoveMandalorianDown()
        self.CheckBoundary()


    def CheckBoundary(self):
        if self._xcoordinate < self.__xlimit[0]:
            self._xcoordinate = self.__xlimit[0]
        elif self._xcoordinate > self.__xlimit[1]:
            self._xcoordinate = self.__xlimit[1]
        if self._ycoordinate < self.__ylimit[0]:
            self._ycoordinate = self.__ylimit[0]
        elif self._ycoordinate > self.__ylimit[1]:
            self.__yvel = 0
            self._ycoordinate = self.__ylimit[1]

    def MoveMandalorianRight(self):
        self._xcoordinate = self._xcoordinate + 2

    def MoveMandalorianLeft(self):
        self._xcoordinate = self._xcoordinate - 2

    def MoveMandalorianUp(self):
        self._ycoordinate = self._ycoordinate - 2
        self.__yvel = 0

    def MoveMandalorianDown(self):
        self._ycoordinate = self._ycoordinate + floor(self.__yvel)
        self.__yvel = self.__yvel + 0.5

    def ActivatShield(self):
        self._shape = [ [" ","\u001b[32m" + "0"," "," "," ","\u001b[32m" + "/"],["\u001b[32m" + "|","\u001b[32m" + "_","\u001b[32m" + "|","\u001b[32m" + "-","\u001b[32m" + "/"," "],["\u001b[32m" + "/","\u001b[32m" + "_","\u001b[32m" + "\\","\u001b[32m" + "_"," "," "]]

    def DeactivateShield(self):
        self._shape = [ [" ","0"," "," "," ","/"],["|","_","|","-","/"," "],["/","_","\\","_"," "," "]]

    def BossLevel(self):
        self.__xlimit = [1,59]
        self._shape = [ [" ","\u001b[36m" + "0"," "," "," ","\u001b[36m" + "/"],["\u001b[36m" + "|","\u001b[36m" + "_","\u001b[36m" + "|","\u001b[36m" + "-","\u001b[36m" + "/"," "],["\u001b[36m" + "/","\u001b[36m" + "_","\u001b[36m" + "\\","\u001b[36m" + "_"," "," "]]
