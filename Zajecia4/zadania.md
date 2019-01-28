# Krotki, słowniki, zbiory i inne

[Słownik](https://docs.python.org/3/library/stdtypes.html#dict)
[Zbiór](https://docs.python.org/3/library/stdtypes.html?highlight=set#set)
[Krotka](https://docs.python.org/3/library/stdtypes.html#tuple)
[Lista](https://docs.python.org/3/library/stdtypes.html#list)
Napisz program, który:

```python
d1 = {}
d1["Piotr"] = 23
d1["Asia"] = 25
d1["Anita"] = 18
d1["Romek"] = 12
d2 = {}
d2["Atomek"] = 14
d2["Janek"] = 16
l1 = [1, 5, 6, 23, 12, 1, 41]
l2 = ['Poniedziałek', 'Wtorek', 'Środy', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
```

1. Wyświetli wszystkie elementy słownika `d1`.
2. Połączy dwa słowniki w jeden `d1` i `d2`. Najpierw stwórz wynikowy słownik pusty `d3`, a następnie dodaj do niego każdy element z `d1` i z `d2`.
3. Zsumuje wszystkie wartości w słowniku `d1`.
4. Wyświetli każdy element listy `l1` razy 2.
5. Zamieni dwie listy na słownik, przy czym elementy pierwszej listy będą kluczami, a drugiej listy wartościami `l1` `l2`.
6. Znajdzie maksimum i minimum z wartości w liście `l1`.
7. Stworzy zbiór `s1` złożony z liczb od 0 do 10.
8. Stworzy krotkę z elementów 11, "listopada", 2018.
9. Znajdzie i wypisze na ekran elementy, który powtarzają się w krotce `(1,2,11,1,1,4)`.
10. Usunie puste krotki z listy krotek, dla wejścia `[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]` zwróci `[('',), ('a', 'b'), ('a', 'b', 'c'), 'd']`.

## Dla znudzonych

Zbliżają się Mikołajki. Mikołaj chodzi już po osiedlu zakradając się do domów.
Sprytny Bajtek zostawił w kominie samoprzylepny nadajnik GPS.
Dzięki niemu jest w stanie śledzić położenia Mikołaja.
Niestety nadajnik nie jest doskonały i w informuje Bajtka jedynie o względnych zmianach położenia Mikołaja.
Informacja, którą dostaje Bajtek przedstawiła się następująco:
```
^^><>>^^^><<<<<^>^>^>^>>V>V^>>V^>V^>V>^>V>^V>^V<^><^V><>^<><>V<<>^^V>^>VV^>>^<>^V<>V^<<><V><^>V<>V<^>V^<<>V^<<>V^<<V>^>><V>^V><>^V<^<^V>V^<^V<>^V>^<>V^><V^><V^<V^><V<V^>^V<>V^<<<>>>>^^^^^VVV^V^V^VV^V^V^V^^V<^>^V>^VV^>^V>VV^<>V^>
```
W jakim miejscu względem domu Bajtka aktualnie znajduje się Mikołaj?
