class Figure:
    def __init__(self,x,y):
        self._x=x
        self.__y=y
Kryg=Figure(3,2)
print(Kryg._x)
print(Kryg._Figure__y)
