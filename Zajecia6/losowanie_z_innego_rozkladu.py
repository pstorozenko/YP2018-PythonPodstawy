import random
import math
import matplotlib.pyplot as plt

l = []
for i in range(1000):
    x = 1 -  random.random() ** 2
    l.append(x)
    print(x)

plt.hist(l)
plt.show()