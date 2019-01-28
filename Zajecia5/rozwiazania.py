def moj_max(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    else:
        return c
    
def pole_kola(r):
    return 3.1416 * r ** 2

def moja_suma(l):
    s = 0
    for e in l:
        s += e
    return s

def moj_iloczyn(l):
    il = q
    for e in l:
        il *= e
    return il

def czy_w_zakresie1(x, a, b):
    if x >= a and x <= b:
        return True
    else:
        return False

def czy_w_zakresie1a(x, a, b): # to też zadziała
    return x >= a and x <= b

def czy_w_zakresie2(x, a, b):
    if x > a and x < b:
        return True
    else:
        return False

def czy_w_zakresie2a(x, a, b): # to też zadziała
    return x > a and x < b

def tylko_unikalne(l):
    return list(set(l))

def minmax(l):
    mi = l[0]
    ma = l[0]
    for e in l:
        if e < mi:
            mi = e
        if e > ma:
            ma = e
    return (mi, ma)

def cumsum(l):
    lw = [l[0]] # lista jednoelementowa
    for i in range(1, len(l)):
        lw.append(lw[i-1] + l[i])
    return lw

from math import sqrt

def czy_pierwsza(x):
    pierwsza = True
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            pierwsza = False
            break
    return pierwsza

def czynniki(n):
    l = []
    p = 2
    while n > 1:
        if n % p == 0:
            l.append(p)
            n //= p
        else:
            p += 1
    return l

def ile_jakich(s):
    male = 0
    duze = 0
    for c in s:
        if c.upper() == c:
            duze += 1
        if c.lower() ==c :
            male += 1
    return (male, duze)

def rysuj_trojkat(n):
    t = [[1,0]]
    for i in range(1,n):
        row = [1]
        for j in range(len(t[i-1]) -1):
            row.append(t[i-1][j] + t[i-1][j+1]) 
        row.append(0)
        t.append(row)
    return t

# na przykład:
# t = rysuj_trojkat(10)
# for l in t:
#     print(l)

def sito_erastotenesa(n):
    l = []
    for i in range(n+1):
        l.append(True)
    # nawet lepiej by było zrobić l = [True] * (n+1) :)
    l[0] = l[1] = False
    for p in range(2,int(sqrt(n) + 1)):
        if l[p] == True:
            for i in range(2 * p, n+1, p):
                l[i] = False
    lw = []
    for i in range(len(l)):
        if l[i] == True:
            lw.append(i)
    return lw

def bin_search(t, x):
    l = 0
    r = len(t) - 1
    s = (l + r) // 2
    while l != r:
        print(l, r)
        s = (l + r) // 2
        if t[s] == x:
            return s
        if t[s] <= x:
            l = s + 1
        else:
            r = s
    if t[l] == x:
        return l
    return -1