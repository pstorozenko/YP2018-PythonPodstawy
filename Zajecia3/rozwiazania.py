print("Listy")

l = [1,2,4,-1,3,21,4]

print("Zad1")
s = 0
for e in l:
    s += e

print(s)

print("Zad 2")
il = 1
for e in l:
    il *= e

print(il)

print("Zad 3")
ma = l[0]
for e in l:
    if e > ma:
        ma = e

print(ma)

print("Zad 4")
l2 = ['Ala', 'ma', 'kota', '.'] 
licz = 0
for e in l2:
    if len(e) > 2:
        licz += 1

print(licz)

print("Zad 5")
lzad5 = []
for i in range(len(l)):
    if i % 2 == 1:
        lzad5.append(l[i])

print(lzad5)

print("Zad 6")
l6 = [[1, 2, 3], [4, 5, 6]] 
lw = []
for e in l6:
    for n in e:
        lw.append(n)

print(lw)

print("Pętle")

print("Zad 1")
for n in range(108, 194 + 1):
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

print("Dla nudzących się")

print("Zad 1")
l = [11, 33, 50] 
res = 0
for e in l:
    res = res * 100 + e

print(res)

print("Zad 2")
l = [1, 2, 3, 4]
napis = "element"
lw = []
for e in l:
    lw.append(napis + str(e))

print(lw)

print("Zad 3")
l =  [10, 200, 3, -42, 102]
nz = 0
for e in l:
    while e > 0:
        if e % 10 == 0:
            nz += 1
        e //= 10
print(nz)

print("Zad 4")
a = 121
b = 14
ost_cyfra = a % 10
for e in range(b):
    ost_cyfra = (ost_cyfra * ost_cyfra) % 10
print(ost_cyfra)

print("Zad 5")
r = 10
c = 3
matrix = []
for e in range(r):
    row = []
    for i in range(c):
        row.append(0)
    matrix.append(row)

print(matrix)

print("Zad 6")
from math import sqrt
l = 1000000007
pierwsza = True
for i in range(2, int(sqrt(l)+1)):
    if l % i == 0:
        pierwsza = False
        break

if pierwsza:
    print("Liczba",l,"jest pierwsza")
else:
    print("Liczba", l, "nie jest pierwsza")