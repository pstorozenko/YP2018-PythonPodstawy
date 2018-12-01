
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def wypisz_punkt(self):
        print("Jestem punktem o współrzędnych", str(self.x), str(self.y))

    def __repr__(self):
        return "Punkt: " + str(self.x) + " " + str(self.y)

class Trojkat:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def wypisz_trojkat(self):
        print("Trojkat:", p1, p2, p3)

p1 = Punkt(1,2)
p2 = Punkt(3,4)
print(p1.x , p1.y)
print(p2.x, p2.y)
p1.wypisz_punkt()
p2.wypisz_punkt()
p3 = Punkt(0,0)
print(p3)
t = Trojkat(p1,p2,p3)
t.wypisz_trojkat()
