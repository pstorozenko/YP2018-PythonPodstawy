class Pracownik:
    def __init__(self, id, imie, nazwisko):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        
    def __repr__(self):
        s = "Pracownik " + str(self.id) + ": " + str(self.imie) + " " + str(self.nazwisko)
        return s


l = []
l.append(Pracownik(1, "Jan", "Nowak"))
l.append(Pracownik(2, "Adam", "Kowalski"))
l.append(Pracownik(3, "John", "Smith"))
print(l)
print(l[2])