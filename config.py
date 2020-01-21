class config:
    def __init__(self):
        self.__framerate = 8
        self.__height = 29
        self.__length = 130
        self.__gameLength = 1000
        self.__gameTime = 200
        self.__winCond = 2000

    def framerate(self):
        return self.__framerate

    def incframerate(self):
        self.__framerate = 20

    def decframerate(self):
        self.__framerate = 8

    def dimensions(self):
        dim = [self.__height,self.__length]
        return dim

    def length(self):
        return self.__gameLength

    def time(self):
        return self.__gameTime

    def winCond(self):
        return self.__winCond
