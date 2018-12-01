import math
def wypisz_siema():
    print("*****************")
    print("SIEMA")
    print("*****************")

def wypisz_n_dziendobry(n):
    for i in range(n):
        print("Dzień dobry")

def odl(x, y):
    d = math.sqrt(x ** 2 + y ** 2)
    print(d)
    return (d, x, y)

def zwroc2():
    return 2

d = odl(4,4)
q = 12
w = 3
print(odl(w,q))

print(zwroc2())