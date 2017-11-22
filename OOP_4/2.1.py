class Point():
    count=0
    def __init__(self,x,y):
        Point.count+=1
        self.x=x
        self.y=y
    @staticmethod
    def who_much_count(count):
        return  Point.__count__
    def __add__(self,point):
         point=Point(self.x + point.x,self.y + point.y)
         return point
p1=Point(2,1)
p2=Point(1,2)
p3=p1+p2
print(p3.x)
print(p3.y)


