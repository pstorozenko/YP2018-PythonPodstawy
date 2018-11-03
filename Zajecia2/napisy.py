napis = "Lubie Jagody"

print(napis)
napis_maly = napis.lower()
print(napis_maly)
napis_duzy = napis.upper()
print(napis_duzy)
print('napis == "Lubie truskawki"', napis == "Lubie truskawki")
print('napis == "Lubie Jagody"', napis == "Lubie Jagody")
print('napis == "lubie Jagody"', napis == "lubie Jagody")
print('napis.find("Jagody")', napis.find("Jagody"))
print('napis.find("jagody")', napis.find("jagody"))

# Jak sprawdzic czy w zdaniu wystepuje jakies slowo?
dlugi_napis = "Ala ma kota"
if dlugi_napis.find("kot") != -1:
    print("W zdaniu")
    print(dlugi_napis)
    print("wystepuje slowo kot")
else:
    print("W zdaniu")
    print(dlugi_napis)
    print("NIE wystepuje slowo kot")

if dlugi_napis.startswith("Ala") == True:
    print("Ta Ala to często jednak pojawia się w przykładach")

if dlugi_napis.endswith("kota") == True:
    print("Ten kot to ma fajnie")
