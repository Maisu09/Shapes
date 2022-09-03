from Rectangle import Rectangle

class Square(Rectangle):
    __length = float()

    def __init__(self, length:float):
        super().__init__(length, length)

        self.__length = length 

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        print("length was set")
        self.__lenght = length
        self.__init__(self.__lenght)

        

    def Display(self):
        return super().Display()