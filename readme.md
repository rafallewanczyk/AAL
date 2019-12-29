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
### Mode 3 - Dodaje dane wygenerowane przez generator oraz dokonuje analizy dla dodania elementu flaga= "-s"
1. jeśli argumentem generatora jest link generator generuje słowa ze strony internetowej,\
w przeciwnym wypadku generator szuka pliku o podanej nazwie
2. np python main.py 1000003 -s slowa.txt
### Mode 4 - Dodaje dane wygenerowane przez generator oraz dokonuje analizy dla enumeracji tablicy flaga= "-e"
1. jeśli argumentem generatora jest link generator generuje słowa ze strony internetowej,\
w przeciwnym wypadku generator szuka pliku o podanej nazwie
2. np python main.py 1000003 -e slowa.txt
### Mode 5 - Dodaje dane wygenerowane przez generator oraz dokonuje analizy dla n wyszykań w tablicy flaga= "-n"
1. jeśli argumentem generatora jest link generator generuje słowa ze strony internetowej,\
w przeciwnym wypadku generator szuka pliku o podanej nazwie
2. np python main.py 1000003 -n slowa.txt
## Rozwiązanie problemu
Szczegółowe informacje w dokumentacji

## Przewodnik po plikach
```
│   main.py 
│   readme.md
│   [AAL] Tablica mieszająca dokumentacja.pdf
│
├───algorithms
│   │   Generator.py - Klasa realizująca genereator 
│   │   HashTable.py - Klasa realizująca tablicę mieszającą 
│   │   __init__.py
│
├───data - przykładowe dane wejściowe o róznych rozmiarach 
│       1000.txt
│       10000.txt
│       100000.txt
│       1000000.txt
│       2000000.txt
│       3000000.txt
│       5000.txt
│       50000.txt
│       500000.txt
│       data_creator.py
│       slowa.txt - plik zawierający ~3mln polskich słów 
│
├───performance_tests - pliki przeprowadzające testy zaprezentowane w dokumentacji
│       add_test05.out
│       add_test05.sh
│       add_test1.out
│       add_test1.sh
│       enum_test05.out
│       enum_test05.sh
│       enum_test1.out
│       enum_test1.sh
│       nsearch_test05.out
│       nsearch_test05.sh
│       nsearch_test1.out
│       nsearch_test1.sh
│       run_all_tests.sh
│
├───test
│       HashTableTest.py - testy jednostkowe tablicy mieszającej 

```
