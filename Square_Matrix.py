import random
def way(choose,size):
    if choose == 1:
        a=[]
        b=[]
        for i in range(size):
            for j in range(size):
                x=random.randint(0,10)
                b.append(x)
            a.append(b)
            b=[]
        return a
    else:
        a=[]
        b=[]
        for i in range(size):
            for j in range(size):
                x=int(input())
                b.append(x)
            a.append(b)
            b=[]
        return a
class Square_Matrix:
   #size=5
   #quantity=10
   def __init__(self,size,choose):

        self.size=size
        self.choose=choose
        self.a=way(choose,size)
   def get (self):
        print(self.size)
   def __str__(self):
        for i in range(self.size):
            s=str(self.a[i]) + "\n"
            return s





SM=Square_Matrix(3,1)
print(SM.a)
SM.get()
print(SM.__str__())
