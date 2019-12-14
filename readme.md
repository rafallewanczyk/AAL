## Wizytówka
Rafał Lewanczyk
293140
## Zadanie
W14, W21, W31\
Analiza oraz implementacja tablicy mieszającej spełniającej następujące założenia:\
    -W przypadku kolizji obliczamy nową lokalizację\
    -Testy przeprowadzić dla: listy słów języka polskiego wygenerowanych z zadanych tekstów\
    -Zastosować jedną funkcję mieszającą; dodatkowo przeprowadzić analizę dla enumeracji tablicy (wydobycia wszystkich elementów).
## Parametry programu
### Pierwszy wymagany argument size - rozmiar tablicy
### Mode 1 - Dane z wejścia standardowego, udostępnia interfejs dla użytkowanika; flaga = "-i"
1. np. python main.py 1000003 -i
### Mode 2 - Dodaje dane wygenerowane przez generator oraz wyswietla zawartość tablicy flaga= "-g"
1. jeśli argumentem generatora jest link generator generuje słowa ze strony internetowej,\
w przeciwnym wypadku generator szuka pliku o podanej nazwie
2. np. python main.py 103 -g https://pl.wikipedia.org/wiki/Rhipidolestes_okinawanus
3. np. python main.py 103 -g slowa.txt 
### Mode 3 - Dodaje dane wygenerowane przez generator oraz dokonuje analizy dla enumeracji tablicy flaga= "-s"
1. jeśli argumentem generatora jest link generator generuje słowa ze strony internetowej,\
w przeciwnym wypadku generator szuka pliku o podanej nazwie
2. np python main.py 1000003 -s slowa.txt

## Rozwiązanie problemu
Szczegółowe informacje w dokumentacji

## Przewodnik po plikach
```
C:.
│   main.py
│   readme.md
│   slowa.txt - plik zawierający ~3000000 polskich slów służacy do tworzenia testów
│
├───algorithms
│   │   Generator.py - klasa realizująca generator
│   │   HashTable.py - klasa realizująca tablice mieszającą
│   │   __init__.py
│
├───data - przydkładowe dane wejściowe skłądające się z polskich słów
│       1000.txt
│       10000.txt
│       100000.txt
│       1000000.txt
│       5000.txt
│       50000.txt
│       500000.txt
├───test
│       HashTableTest.py - Testy jednostkowe funkcji tablicy mieszającej
```
