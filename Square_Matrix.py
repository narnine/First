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
   size=4
   quantity=10
   def __init__(self,size,choose):

        self.size=size
        self.choose=choose
        self.a=way(choose,size)
   def get (self):
        print(self.size)
   def __str__(self):
        for i in range(self.size):
            s=str(self.a[i]) + "\n"
            print(1)
            return s
   def _import(self):
        b=int()
        for i in range(self.size):
            b=self.a[i][i]+b
        print(b)
   def transposition(self):
        for i in range(self.size):
            for j in range(self.size):
                self.a[i+1][j]=self.a[j][i+1]
        return self.a



SM=Square_Matrix(2,1)
print(SM.a)
SM.get()
print(SM.__str__())
SM._import()
SM.transposition()
