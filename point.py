class Point:
    def __init__(self,x,y):
        self._x = float(x)
        self._y = float(y)


    def add( self, b ):
        return Point( self._x + b.getX(), self._y + b.getY() )


    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, newValue):
        self._x = float(newValue)

    def setY(self, newValue):
        self._y = float(newValue)


    def reset(self):
        self._x = 0
        self._y = 0

    def move(self, posx, posy):
        self._x = posx
        self._y = posy


