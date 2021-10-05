#Steg   1 skapa en klass
#       2 def __init__ ska ta self 
#       3 i def __init__ skapa properties med _ prefix
#       3.5 properties typecastas (konverteras till rätt typ) 
#       4 fundera om valid state dvs måste man skicka in nåt

class Rectangle:
    def __init__(self, height, width):
        self._height = float(height)
        self._width = float(width)

    def calculateArea(self):    
        return self._height * self._width