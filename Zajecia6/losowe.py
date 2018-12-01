import random

prog = 0.1
n = 1000
n_ponizej = 0

for i in range(n):
    p = random.random() # zwraca losową liczbę z przedziału 0,1
    if p < prog:
        n_ponizej += 1

print(n_ponizej / n) # procent liczb wylosowanych, mniejszych od progu
