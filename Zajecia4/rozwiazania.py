d1 = {}
d1["Piotr"] = 23
d1["Asia"] = 25
d1["Anita"] = 18
d1["Romek"] = 12
d2 = {}
d2["Atomek"] = 14
d2["Janek"] = 16
l1 = [1, 5, 6, 23, 12, 1, 41]
l2 = ['Poniedziałek', 'Wtorek', 'Środy', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']

print("Zad 1")

for e in d1:
    print(e, d1[e])

print("Zad 2")
d3 = {}
for e in d1:
    d3[e] = d1[e]
for e in d2:
    d3[e] = d2[e]
print(d3)

print("Zad 3")
s = 0
for e in d1:
    s += d1[e]

print(s)

print("Zad 4")
for e in l1:
    print(e, e)

print("Zad 5")
d5 = {}
for i in range(len(l2)):
    d5[l2[i]] = l1[i]

print("Zad 6")
mi = l1[0]
ma = l1[0]
for e in l1:
    if e < mi:
        mi = e
    if e > ma:
        ma = e
print("Min", mi, "Max", ma)
# Można użyć również po prostu max(l1), min(l1) :)

print("Zad 7")
s1 = set(range(11))
print(s1)

print("Zad 8")
t = ( 11, "listopada", 2018)
print(t)

print("Zad 9")
t2 = (1,2,11,1,1,4)
s2 = set()
for e in t2:
    if e in s2:
        print("element", e, "powtarza się")
    else:
        s2.add(e)

print("Zad 10")
l =  [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')] 
lw = []
for e in l:
    if len(e) > 0:
        lw.append(e)
print(lw)

print("Zadanie bonusowe")
s = "^^><>>^^^><<<<<^>^>^>^>>V>V^>>V^>V^>V>^>V>^V>^V<^><^V><>^<><>V<<>^^V>^>VV^>>^<>^V<>V^<<><V><^>V<>V<^>V^<<>V^<<>V^<<V>^>><V>^V><>^V<^<^V>V^<^V<>^V>^<>V^><V^><V^<V^><V<V^>^V<>V^<<<>>>>^^^^^VVV^V^V^VV^V^V^V^^V<^>^V>^VV^>^V>VV^<>V^>"
d = {}
for c in s:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
print("Dom znajduje się w miejscu o współrzędnych", d['^'] - d['V'], "i", d[">"]- d["<"] )