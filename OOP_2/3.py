class Figure:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def set_radius(self,radius2):
       self.__radius = radius2
       radius=property(set_radius,3)
Kryg=Figure(3,2)
Kryg.radius=5
