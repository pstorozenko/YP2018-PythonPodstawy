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
