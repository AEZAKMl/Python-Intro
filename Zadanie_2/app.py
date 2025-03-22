import re
from datetime import datetime


def czy_email_poprawny(email):
    if not email:
        return False

    wzorzec_emaila = r'^[^@]+@[^@]+\.[^@]+$'

    dopasowanie = re.match(wzorzec_emaila, email)
    return dopasowanie is not None


def oblicz_pole_trojkata(podstawa, wysokosc):
    """
Oblicz pole trójkąta ze wzoru (a * h) / 2.
Podstawa i wysokość muszą być większe od zera.
"""

    if podstawa <= 0 or wysokosc <= 0:
        raise ValueError("Podstawa i wysokość muszą być większe od zera")

    return (podstawa * wysokosc) / 2


def przetworz_liste(lista):
    """
Zwraca posortowaną rosnąco listę liczb większych lub równych 10.
"""
    liczby = [x for x in lista if x >= 10]
    return sorted(liczby)


def konwertuj_date(data_str):
    """
    Konwertuj datę z formatu dd-mm-yyyy lub dd.mm.yyyy
    na format yyyy/mm/dd.
    """

    if not data_str:
        raise ValueError("Data nie może być pusta")

    dozwolone_formaty = ["%d-%m-%Y", "%d.%m.%Y"]

    for forma in dozwolone_formaty:
        try:
            data = datetime.strptime(data_str, forma)
            return data.strftime("%Y/%m/%d")
        except ValueError:
            continue

    raise ValueError("Nieprawidłowy format daty. Poprawny format to dd-mm-yyyy lub dd.mm.yyyy")


def czy_palindrom(tekst):
    """
    Sprawdza, czy dany tekst jest palindromem.
    Ignoruje wielkość liter i spacje.
    """

    oczyszczony = tekst.replace(" ", "").lower()
    return oczyszczony == oczyszczony[::-1]
