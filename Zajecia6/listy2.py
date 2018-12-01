import time
import random

l = []
for i in range(10):
    l.append(i)

while (len(l) > 0):
    print(l)
    ind = random.randint(0, len(l)-1)
    del l[ind]
    time.sleep(1)
    
