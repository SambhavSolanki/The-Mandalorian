from colorama import Fore, Back, Style , init
from random import randint

class grid:

    def __init__(self,height,length):
        self.__length = length
        self.__height = height
        self.__grid = []
        for i in range(self.__height):
            curr = []
            for j in range(self.__length):
                curr.append(" ")
            self.__grid.append(curr)

    def printgrid(self):
        for i in range(self.__height):
            for j in range(self.__length-30):
                if (i <3) or (i>= (self.__height - 3)):
                    print('\033[1m' + Back.WHITE + self.__grid[i][j],end=''),
                else:
                    print('\033[1m' + Fore.WHITE + Back.BLACK + self.__grid[i][j],end=''),
            print(Style.RESET_ALL)

    def AddToGrid(self,y,x,a):
        self.__grid[y][x] = a

    def ClearGrid(self):
        for i in range(self.__height):
            for j in range(self.__length):
                self.__grid[i][j] = " "
