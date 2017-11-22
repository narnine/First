class A:
    def getx(self):
       return self.__x*3
    def setx(self, value):
       self.__x = value
    def delx(self):
       del self.__x
    x = property(getx, setx, delx, "I'm good string.")
B=A()
B.x= "I'm bad string."
print(B.x)
del B.x




