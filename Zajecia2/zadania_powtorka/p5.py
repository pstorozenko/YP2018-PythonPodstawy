rok = input("Podaj rok: ")
rok = int(rok)

przestepny = 0

if rok % 4 == 0:
    przestepny = 1
    if rok % 100 == 0:
        przestepny = 0
        if rok % 400 == 0:
            przestepny = 1

if przestepny == 0:
    print("Rok", rok, "nie jest przestępny")
else:
    print("Rok", rok, "jest przestępny")
