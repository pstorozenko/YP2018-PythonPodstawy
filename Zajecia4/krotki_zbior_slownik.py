# Krotki tuple

t = (3, 5)
print(t)
print(t[0])
print(t[1])

print("******************")
# Zbiory set
s = set([(0,0), (1,1), (2,0)])
print(s)
for e in s:
    x = e[0]
    y = e[1]
    print("Element", e)
    print("Pierwsza współrzędna to", x)
    print("Druga współrzędna to", y)
    print()
    


print("******************")
s.add((3,1))
s.add("Pomidor")
print(s)

if (0, 1) in s:
    print((0, 1), "jest w zbiorze")
else:
    print((0, 1), "nie ma w zbiorze")
print("******************")
s2 = set([1,2,7,1,1,3,2,5])
print(s2)
for e in s2:
    print(e)

# Słowniki
d = {}
d["Piotr"] = 23
d["Asia"] = 25
d["Anita"] = 18
d[("Romek", "Atomek")] = 12
d["Janek"] = [100, 110]
print(d)
