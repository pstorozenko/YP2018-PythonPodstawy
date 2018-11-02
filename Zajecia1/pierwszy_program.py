# Wypisywanie na ekran
print("Hello world")

# Wykorzystywanie zmiennych
x = 12      # Zmienna całkowito liczbowa
y = 3.14    # Zmienna zmiennoprzecinkowa
print(x * y)

a = 6e24    # Zmienna zmiennoprzecinkowa w postaci wykładniczej. 6 i 24 zera
print(a)
print((a + 1000) - a)


z = 17
print("Dzielenie", z / 2)
print("Dzielenie całkowite", z // 2)
print("Dodawanie", z + 2)
print("Odejmowanie", z - 2)
print("Potegowanie", z ** 2)
print("Reszta z dzielenia", z % 2)

# Wynik działania przypisany do zmiennej
abc = (x * y) / z
print(abc)

# Wczytywanie zmiennej od użytkowanika
imie = input("Podaj swoje imie: ")
print("Cześć", imie)

# Warto pamiętać, że zmienna wczytywana jest jako napis, więc musimy zamienić ją na liczbę
wiek = input("Podaj ile masz lat: ")
wiek_cal = int(wiek)
print("Za 5 lat będziesz miał" , wiek_cal + 5)

# Instrukcja warunkowa
if wiek_cal < 20: # > >= == <= < !=
    print("Jesteś nastolatkiem")
else:
    print("Nie jesteś nastolatkiem")

# > mniejsze
# >= mniejsze równe
# == równe
# <= większe równe
# < większe
# != różne

# Wypisanie wartości logicznej, "Czy zmienna wiek_cal jest równa 23?"
print(wiek_cal == 23)

# Instrukcja if bez else
if wiek_cal > 100:
    print("Jesteś stary")

# Koniunkcja czyli połączenie dwóch warunków w i
if wiek_cal > 30 and wiek_cal < 60:
    print("Jesteś w średnim wieku")

# Alternatywa czyli połączenie dwóch warunków w lub
if wiek_cal < 0 or wiek_cal > 200:
    print("Chyba mnie oszukujesz...")
