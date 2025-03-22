# my_awesome_lib

my_awesome_lib to prosta biblioteka w Pythonie, która oferuje funkcje do:
- Obsługi danych: filtrowanie liczb parzystych oraz sumowanie elementów listy.
- Operacji matematycznych: odejmowanie liczb oraz potęgowanie.
- Przetwarzania tekstu: odwracanie ciągów znaków i liczenie słów.

Instalacja:

Bibliotekę możesz zainstalować na dwa sposoby:

  1. Instalacja ręczna
Skopiuj cały folder `my_awesome_lib` do swojego projektu.

  2. Instalacja przy użyciu `setup.py`
Jeżeli posiadasz plik `setup.py`, zainstaluj bibliotekę w trybie developerskim:
```bash (Terminal)
pip install -e .


Poniżej przykładowy kod pokazujący, jak korzystać z funkcji dostępnych w bibliotece:

- Importowanie modułów
from my_awesome_lib import data_utils, math_tools, text_processing

- Przykłady z data_utils
dane = [1, 2, 3, 4, 5, 6]
parzyste = data_utils.filter_even(dane)
print("Liczby parzyste:", parzyste)        # Oczekiwany wynik: [2, 4, 6]

suma = data_utils.sum_data(dane)
print("Suma danych:", suma)                # Oczekiwany wynik: 21

- Przykłady z math_tools
wynik_odejmowania = math_tools.subtract(10, 3)
print("Wynik odejmowania:", wynik_odejmowania)  # Oczekiwany wynik: 7

wynik_potegowania = math_tools.power(2, 3)
print("Wynik potęgowania:", wynik_potegowania)    # Oczekiwany wynik: 8

- Przykłady z text_processing
odwrocony = text_processing.reverse_text("Python")
print("Odwrócony tekst:", odwrocony)        # Oczekiwany wynik: "nohtyP"

liczba_slow = text_processing.count_words("Hello world!")
print("Liczba słów:", liczba_slow)           # Oczekiwany wynik: 2



Licencja:
Projekt udostępniony na licencji XYZ

Autor i Wersja:
Autor: Dorian Kozłowski

Wersja: 0.1 beta

Data: 2012-12-12
