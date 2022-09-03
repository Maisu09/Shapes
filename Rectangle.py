from Shapes import Shapes

class Rectangle(Shapes):

    def __init__(self, width:float, length:float):
        super().__init__(width * length, width + length)
        self.__width = width
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        print("setter was used")
        self.__length = length
        self.__init__(self.__width, self.__length)

    @property
    def width(self):
        return self.width

    def Display(self):
        return super().Display()
