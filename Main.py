from Shapes import Shapes
from Circle import Circle
from Rectangle import Rectangle
from Square import Square

def main():
    shape = Shapes(5.6, 1)
    shape.Display()

    print("rectangle object:")
    rectangle = Rectangle(3, 4)
    rectangle.Display()
    rectangle.length = 23.3
    print(rectangle.length)
    rectangle.Display()

    print("\ncircle object:")
    circle = Circle(4)
    circle.Display()
    print(circle.radius)
    circle.radius = 25
    circle.Display()

    
    print("\nSquare object:")
    square = Square(5)
    square.Display()
    print(square.length)    
    square.length = 4
    square.Display()


if __name__ == '__main__' :
    main()