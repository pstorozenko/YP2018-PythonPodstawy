# Zad 1
s = 0
l = [1,2,3,4,5,6,42,7]
for e in l:
    s = s + e
print("Suma wynosi", s)

# Zad 2
il = 1
for e in l:
    il = il * e
print("Iloczyn wynosi", il)

# Zad 3
m = l[0]
for e in l:
    if e > m:
        m = e
print("Element maksymalny wynosi", m)

# Zad 4
l = ['Ala', 'ma', 'kota', '.']
n = 0
for e in l:
    if len(e) > 2:
        n = n + 1
print("Lista", l, "zawiera", n, "napisów o długości większej niż 2")

# Zad 5
lw = []
for i in range(len(l)):
    if i % 2 != 0:
        lw.append(l[i])
print("Elementy listy", l, "na nieparzystych indeksach to: ", lw)

