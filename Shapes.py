class Shapes:
    __area = float()
    __perimetre = float()

    def __init__(self, area, perimetre):
        self.__area = area
        self.__perimetre = perimetre
    
    @property
    def area(self):
        return self.__area
    
    @property
    def perimetre(self):
        return self.__perimetre

    def Display(self):
        print(self.__area, self.__perimetre)
    
