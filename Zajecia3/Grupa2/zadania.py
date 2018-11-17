print("Zad 1")
l = [1, 42, 23, 61, -12]
s1 = 0
for e in l:
    s1 = s1 + e
print("Suma:", s1)

s2 = 0
for i in range(len(l)):
    s2 = s2 + l[i]
print("Suma:", s2)

print("Zad 2")
il = 1
for e in l:
    il = il * e
print("Iloczyn:", il)

print("Zad 3")
m = l[0]
for e in l:
    if e > m:
        m = e

for zabka in l:
    print(zabka)
print("Maksymalny element listy wynosi:", m)

# Zad3a -- Znajdź minimalny element w liście

print("Zad 4")
l = ['Ala', 'ma', 'kota', '.']
c = 0
for e in l:
    if len(e) > 2:
        c = c + 1
print("Lista", l, "posiada", c, "słów dłuższych niż 2 znaki")

print("Zad 5")
l = [4, 1, 23, 10, 12, 52] # ma zostać wypisane 1,10,52
for i in range(len(l)):
    if i % 2 != 0:
        print("Pod indeksem", i, "jest", l[i])

print("Zad 6")
l = [[1, 2, 3], [4, 5, 6]]
print(l)
print(len(l))
lw = []
for e in l:
    print(e)
    for n in e:
        lw.append(n)
print(lw)


## Pętla for

print("Zad 1")
for n in range(108, 194+1):
    if n % 17 == 0:
        print(n)

print("Zad 2")

for i in range(5):
    print((i+1) * "* ")
for i in range(4,0,-1):
    print(i * "* ")

print("Zad 3")
for i in range(1,10):
    s = i
    for j in range(i-1):
        s = s * 10 + i
    print(s)

for i in range(1,10):
    n = str(i)
    print(i * n)

print("Zad 4")
for n in range(7, 17 + 1):
    if n == 13 or n == 15:
        continue
    print(n)