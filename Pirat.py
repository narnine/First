import random
import math


class Yoxoxo:
    def __init__(self,name,boat_weight):
        pirat_gold = 0
        pirat_conjuration = 0
        empty = 0
        print("Твое имя моряк?")
        self.name = name
        print(self.name)
        print("Cколько коряга весит?")
        self.boat_weight = boat_weight
        print(self.boat_weight)
        if self.boat_weight > 60:
            print("ООО толстенькая!")
            while self.boat_weight > 60:
                print("Cколько коряга весит?")
                self.boat_weight=int(input())
                print(self.boat_weight)
        print()

    def open(self):
        sum_weight = 0
        count1 = 0
        while sum_weight < self.boat_weight:
            a = Chest()
            sum_weight = a.weight + sum_weight
            if a.choose == 1:
                self.pirat_gold = self.pirat_gold + a.gold
            elif a.choose == 2:
                self.pirat_conjuration = self.pirat_conjuration + a.conjuration
            elif a.choose == 3:
                self.empty+=1
            count1+=1
        print(count1)


def rich(pirat1,pirat2,pirat3,pirat4):
    name_rich1 = " "
    name_rich2 = " "
    big_rich=0
    l=[pirat1,pirat2,pirat3,pirat4]
    for i in range(0,4):
        if l[i].pirat_gold >= big_rich:
            big_rich = l[i].pirat_gold
            name_rich1 = l[i].name
    print('Имя богатого:' ,name_rich1 ,'Кол-во золото:', big_rich)
    for i in range(0,4):
            if l[i].pirat_gold == big_rich and l[i].name != name_rich1:
                name_rich2 = l[i].name
                print('Имя второго богатого:', name_rich2 ,'Кол-во золото:', big_rich)

def damn(pirat1,pirat2,pirat3,pirat4):
    name_sick1=" "
    name_sick2=" "
    big_conjuration=0
    g=[pirat1,pirat2,pirat3,pirat4]
    for i in range(0,4):
        if g[i].pirat_conjuration >= big_conjuration:
            big_conjuration = g[i].pirat_conjuration
            name_sick1 = g[i].name
    print('Имя больного:' ,name_sick1,'Сколько болел:', big_conjuration)
    for i in range(0,4):
            if g[i].pirat_conjuration == big_conjuration and g[i].name != name_sick1:
                name_sick2 = g[i].name
                print('Имя второго больного:', name_sick2 ,'Сколько болел:', big_conjuration)

def unlucky(pirat1,pirat2,pirat3,pirat4):
    name_unlucky1=" "
    name_unlucky2=" "
    big_unlucky=0
    k=[pirat1,pirat2,pirat3,pirat4]
    for i in range(0,4):
        if k[i].empty >= big_unlucky:
            big_unlucky = k[i].empty
            name_unlucky1 = k[i].name
    print('Имя невезучего:' ,name_unlucky1)
    for i in range(0,4):
            if k[i].empty == big_unlucky and k[i].name != name_unlucky1:
                name_unlucky2 = k[i].name
                print('Имя второго невезучего:', name_unlucky2 )

class Chest:
    gold=0
    def __init__(self):
        self.weight = random.randint(4,10)
        self.choose = random.randint(1,3)
        if self.choose == 1:
            self.gold = random.randint(15,100)
        elif self.choose == 2:
            self.conjuration = random.randint(3,10)
        elif self.choose == 3:
            self.gold = 0

pirat1 = Yoxoxo("ШИШШИ",45)
pirat2 = Yoxoxo('Малыш-били',45)
pirat3 = Yoxoxo('Джек',45)
pirat4 = Yoxoxo('Воробей',45)
pirat1.open()
pirat2.open()
pirat3.open()
pirat4.open()
rich(pirat1,pirat2,pirat3,pirat4)
damn(pirat1,pirat2,pirat3,pirat4)
unlucky(pirat1,pirat2,pirat3,pirat4)
