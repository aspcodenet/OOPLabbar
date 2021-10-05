class Point:
    def __init__(self,x,y):
        self._x = float(x)
        self._y = float(y)


    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, newValue):
        self._x = float(newValue)

    def setY(self, newValue):
        self._y = float(newValue)

