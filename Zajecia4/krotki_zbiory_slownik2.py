# Krotki
x = (12, 42, 3)
print(x)
print("Element 0",x[0])
print("Element 2", x[2])
print("Długość krotki", len(x))

for l in x:
    print(l)
# NIEMODYFIKOWALNE

# Zbiór
s = set([(1, 2), (3,1), (-3,1)])

for k in s:
    print(k)

print("Zawartość zbioru przed dodaniem elementu", (5,1))
print(s)
s.add( (5,1) )
print("Zawrtość zbioru po dodaniu elementu", (5,1))
print(s)
print("Ilość elementów w zbiorze", len(s))
print((0,0) in s)

# Słownik
d = {} # albo d = dict()
d[2] = "Jan"
d[12] = "Niezbędny"
print(d)
