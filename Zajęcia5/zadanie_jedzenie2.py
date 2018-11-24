d = {}

for i in range(5):
    imie = input("Podaj imię: ")
    potrawa = input("Podaj potrawę: ")
    d[imie] = potrawa

for i in range(2):
    imie = input("Czyje upodobania kulinarne chciałbyś poznać?")
    if imie in d:
        jedzenie = d[imie]
        print("Ulubiona potrawą", imie, "jest", jedzenie)
    else:
        print("Niestety nie wiem co lubi jeść", imie)