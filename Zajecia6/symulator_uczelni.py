import random

class Student:
    def __init__(self, imie):
        self.imie = imie
        self.rok_studiow = 1
        self.umiejetnosci = 1 -  random.random() ** 3
    
    def __repr__(self):
        return self.imie + " na roku " + str(self.rok_studiow)

studenci = []
n = 30
for i in range(n):
    studenci.append(Student("Bajtek"))