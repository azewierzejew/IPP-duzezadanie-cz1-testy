Należy podmienić plik map_main.c na ten mój, a następnie porównać in/out z testami.

Plik test.in to test przykładowy z map_main.c dostarczonego przez prowadzących.

Plik map_main.c raczej nie powinien sam z siebie powodować wycieków pamięci.

Czego moje testy nie sprawdzają:
* obsługa wielu map,
* sprawdzanie poprawności nazw miast,
* mogą nie sprawdzać idealnie poprawności wyszukiwania dróg krajowych.

Outy oczywiście mogą nie być poprawne.


Format wejścia:

Kolejne linie opisują poszczególne komendy w następujący sposób.

`nazwakomendy;arg1;arg2;...;argn`

gdzie n – liczba argumentów dla komendy.

Argumenty muszą być w tej samej kolejności, co argumenty dla odpowiednich funkcji w map.h.

Wielkość liter ma znaczenie, więc należy wpisać addRoad, a nie addroad itd.

Białe znaki również mają znaczenie – nie należy dorzucać dodatkowych pomiędzy argumentami/średnikami itd.

W pliku wejściowym mogą znajdować się puste linie (zostaną one zignorowane) oraz komentarze (wiersze rozpoczynające się od znaku #).
