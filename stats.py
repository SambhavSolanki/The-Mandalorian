class stats:
    def __init__(self):
        self.__score = 0
        self.__distance = 0
        self.__lives = 3

    def GetLives(self):
        return self.__lives

    def GetScore(self):
        return self.__score

    def GetDistance(self):
        return self.__distance

    def UpdateDistance(self):
        self.__distance = self.__distance + 1

    def UpdateScore(self):
        self.__score = self.__score + 100

    def UpdateLives(self):
        self.__lives = self.__lives - 1

        
