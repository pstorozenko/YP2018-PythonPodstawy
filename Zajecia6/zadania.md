# Zadania

## Punkty i trójkąty

Do klasy `Punkt` dodaj metody:

* `odleglosc_od_00` - zwróci odległość punktu od punktu 0,0
* `wypisz` - w ładnym formacie wypisze opis punktu na ekran

Do klasy `Trojkat` dodaj metody:

* `wypisz` - w ładnym formacie wypisze opis trójkąta na ekran
* `obwod` - zwróci obwód trójkąta
* `czy_w_srodku` - sprawdzi czy punkt znajduje się w środku trójkąta czy poza
http://www.math.us.edu.pl/pgladki/faq/node105.html
http://matematyka.pisz.pl/strona/1223.html

## Symulator uczelni

Stwórz klasę `Student`.

Klasa posiada składowe:

* `imie` - imię studenta
* `rok_studiow` - informacja na którym student jest roku
* `umiejetnosci` - wartość losowa od 0 do 1 umiejętność studenta do zaliczenia roku
* Konstruktor ustawiający powyższe wartości
* Metodę `__repr__`, która ładnie wypisze studenta

Stwórz listę `n` studentów, każdy student posiada losowo wybrane umiejętności.
Stwórz listę o długości 4, opisującą ile jest studentów na każdym z lat.

Co sekundę:

* Każdy student przechodzi na kolejny semestr z prawdopodobieństwem `umiejetnosci`.
    * Jeżeli student nie zda na kolejny rok, a jest na pierwszym roku to jest wyrzucany z uczelni.
    * Jeżeli student dotrwa do piątego roku to wypisz mu imienne gratulacje i usuń go z listy.
* Wypisz ile studentów jest na którym roku.

Do tego zadania zobacz pliki `random.py`, a później `listy2.py` i `losowanie_z_innego_rozkladu.py`.