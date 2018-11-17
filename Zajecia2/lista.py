l = [1, 2, 3, 4, 12, 42]
print(l[0])
print(l[5])

l[5] = 121
print(l)
print("******************")
print("Sposób 1")
for e in l:
    print(2 * e) 

print("Sposób 2")
for i in range(len(l)):
    print(2 * l[i])

l.append(3.1415)

print(l)

for i in range(10):
    print(i)

for i in range(10, 16):
    print(i)
    
for i in range(2,9,3):
    print(i)
    
for i in range(10):
    if i == 6:
        continue
    print(i)

    
for i in range(10):
    if i == 6:
        break
    print(i)
