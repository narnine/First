class Figure:
    def __init__(self,radius,x,y):
        self.radius=radius
        self.x=x
        self.y=y
    def compare(self,different):
        if self.radius==different.radius:
            print('True')
        else:
            print('False')
Kryg=Figure(5,4,2)
Kvadrat=Figure(5,4,2)
Kryg.compare(Kvadrat)


