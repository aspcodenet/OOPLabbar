from point import Point
from rectangle import Rectangle 


while True:
    width = float(input("Skriv in bredd på en rektangel"))
    height = float(input("Skriv in height på en rektangel"))
    rect = Rectangle(height,width)
    area = rect.calculateArea()
    print(f"Arean blev {area}")


a = Point(10, 20)
#   a.x = "1234"

a.setX(12)
a.setY(111)

print(a.getX())
print(a.getY())


b = 123



