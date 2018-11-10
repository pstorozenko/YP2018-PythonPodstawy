# zad 1
print(2 * 7 * 722287)
# zad 2
a = int(input("Podaj 1. bok trójkąta: "))
b = int(input("Podaj 2. bok trójkąta: "))
c = int(input("Podaj 3. bok trójkąta: "))
if a+b>c and a+c>b and b+c>a:
    print("Nierówność trójkąta spełniona")
else:
    print("Nierówność trójkąta nie spełniona")
# zad 3
zespol = input("Podaj swój ulubiony zespół")
print("WIWAT", zespol.upper())
# zad 4
imie = input("Jak masz na imię?")
if imie.endswith("a") and imie.lower() != "kuba":
    print("Dzień dobry Pani")
else:
    print("Dzień dobry Panu")
# zad 5
odp = input("Ile wynosi 2+2*2?: ")
if int(odp) == 6:
    print("Poprawna odpowiedź :)")
else:
    print("Zła odpowiedź :(")
# zad 6
skala = input("Jaką skale chcesz zamienić C czy F?")
temp = int(input("Podaj jaką chcesz temperaturę zamienić"))
if skala == "C":
    print(2/9 * temp + 32, "stopni F")
else:
    print(5/9 * (temp - 32), "stopni C")

    
