'''
Dorian Kozłowski
Numer Albumu: 152721
'''

# enumerate(iterable, start=0)
# Zwraca obiekt typu enumerate. Argument iterable musi być sekwencją,
# iteratorem lub innym obiektem obsługującym iterację.
# Metoda __next__() iteratora zwróconego przez enumerate() zwraca
# krotkę zawierającą kolejny licznik (zaczynając od wartości start, która domyślnie wynosi 0)
# oraz wartości uzyskane podczas iterowania po iterable.
# https://docs.python.org/3/library/functions.html#enumerate

# Moduł: math
# Ten moduł zapewnia dostęp do funkcji matematycznych zdefiniowanych przez standard C.
# https://docs.python.org/3/library/math.html#module-math

# Wyjątek ZeroDivisionError
# Zgłaszany, gdy drugi argument operacji dzielenia lub operacji modulo wynosi zero.
# Powiązana wartość to ciąg znaków wskazujący typ operandów oraz wykonywaną operację.
# https://docs.python.org/3/library/exceptions.html#ZeroDivisionError




# Program:
# 1. Tworzenie dwóch list i łączenie ich funkcją zip().
# 2. Wykorzystanie jednej funkcji (choice) z wybranego modułu Pythona (moduł random).
# 3. Obsługę wyjątku try-except.

import random  # Moduł do generowania liczb losowych: https://docs.python.org/pl/3/library/random.html#module-random

def main():  # Tworzenie funkcji https://docs.python.org/3/tutorial/controlflow.html#defining-functions
    # Tworzenie dwóch list:
    list1 = [8, 7, 6, 5]
    list2 = [1, 2, 3, 4]

    # Funkcja zip() łączy elementy z iterowalnych obiektów w pary krotki.
    # Dokumentacja: https://docs.python.org/pl/3/library/functions.html#zip
    zipped_lists = list(zip(list1, list2))

    # Użycie funkcji choice() z modułu random do wybrania losowego elementu z listy.
    # Dokumentacja: https://docs.python.org/pl/3/library/random.html#random.choice
    random_element = random.choice(list1 + list2)

    # Obsługa wyjątku przy użyciu try-except:
    try:
        # Próba pobrania elementu o indeksie wykraczającym poza rozmiar listy
        # spowoduje zgłoszenie wyjątku IndexError.
        out_of_range_value = zipped_lists[10]
    except IndexError as e:
        print("Wystąpił błąd IndexError:", e)

    # Wyświetlenie wyników
    print("Połączone listy (zipped_lists):", zipped_lists)
    print("Wylosowany element z obu list:", random_element)

if __name__ == "__main__":
    main()

# Funkcja main() zawiera główny kod programu,
# który uruchamia się tylko wtedy, gdy plik zostanie odpalony bezpośrednio, a nie importowany.
# Dokumentacja: https://docs.python.org/3/library/__main__.html