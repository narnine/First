class Animal():
    def __intit__(self,age,name):
        self.age=age
        self.name=name

class Predator(Animal):
    def bit(self,victim):
         if isinstance(victim,Mammal):
            victim.die()



class Tiger(Predator):
    pass

class Mammal(Animal):
    def die(self):
        del self

class Zebra(Mammal):
    pass

tiger=Tiger(Nelya,16)
zebra=Zebra(Vasy,16)
print(tiger.bit(zebra)
