import math
def pitagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

x = pitagoras(3,4)
print(x)

print(pitagoras(5,12))

def moj_max(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    else:
        return c

print(moj_max(3,4,5))

def moja_transofrmacja(x):
    return 3 * x + 1 # z reguły tak robimy

def moja_transofrmacja2(x):
    print(3 * x + 1) # tak raczej nie


print(moja_transofrmacja(3))

l = []
for i in range(5):
    l.append(moja_transofrmacja(i))

print(l)

l2 = []
for i in range(5):
    l2.append(moja_transofrmacja2(i))

print(l2)
