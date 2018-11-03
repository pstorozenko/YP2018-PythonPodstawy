l = [1, 2, 3, 4, 12, 42]
print(l[0])
print(l[5])

l[5] = "Napis"
print(l)
print("******************")
print("Sposób 1")
for e in l:
    print(2 * e) # napis *2 wydłużna napis dwukrotnie

print("Sposób 2")
for i in range(len(l)):
    print(2 * l[i])

l.append(3.1415)

print(l)