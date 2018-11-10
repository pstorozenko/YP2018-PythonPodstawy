# Zad 1
print(2 * 7 * 722287)

# Zad 2
b1 = int(input("Podaj długość 1. boku"))
b2 = int(input("Podaj długość 2. boku"))
b3 = int(input("Podaj długość 3. boku"))

if b1 + b2 > b3 and b2 + b3 > b1 and b1 + b3 > b2:
    print("Odcinki", b1, b2, b3, "mogą tworzyć trójkąt")

# Zad 3
zespol = input("Jaki jest Twój ulubiony zespół?")
print("WIWAT", zespol.upper())

# Zad 4
imie = input("Jak masz na imię? ")
if imie.endswith("a") and imie.lower() != "kuba":
    print("Dzień dobry Pani")
else:
    print("Dzień dobry Panu")

# Zad 5
odp = input("Jak ma na nazwisko prowadzący zajęcia? ")
if odp.lower() == 'storożenko':
    print("Tak jest!")
else:
    print("Niestety zła odpowiedź")

# Zad 6
skala = input("Podaj z jakiej skali chcesz zmienić temperaturę C/F")
temp = int(input("Jaką temperaturę chcesz zamienić?"))
if skala == "C":
    print("Temperatura w *F", temp*9/5 + 32)
else:
    print("Temperatura w *C", (temp- 32)*5/9)