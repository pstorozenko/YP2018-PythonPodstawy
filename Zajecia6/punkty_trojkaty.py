import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def odleglosc_od_00(self):
        return math.sqrt(self.x**2 + self.y**2)

    def wypisz(self):
        print("Punkt o współrzędnych (", self.x, ",", self.y, ")")

    def __repr__(self):
        return "Punkt o współrzędnych (" + str(self.x) + "," + str(self.y) + ")"

    def odleglosc_od_punktu(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y)**2)


class Trojkat:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def wypisz(self):
        print("Trójkąt:")
        print(self.p1, self.p2, self.p3)
    
    def obwod(self):
        ob = self.p1.odleglosc_od_punktu(self.p2) + self.p1.odleglosc_od_punktu(self.p3) + self.p2.odleglosc_od_punktu(self.p3)
    

p1 = Punkt(1,2)
print(p1.odleglosc_od_00())
p1.wypisz()

p2 = Punkt(3,4)
print(p2.odleglosc_od_punktu(p1))
p2.wypisz()

p3 = Punkt(3,3)
print(p3.odleglosc_od_punktu(p2))

t1 = Trojkat(p1,p2,p3)
t1.wypisz()