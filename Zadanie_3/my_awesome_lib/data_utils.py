def filter_even(data):
    """
    Zwraca nową listę zawierającą tylko liczby parzyste z przekazanej listy 'data'.
    Przykład:
        filter_even([1, 2, 3, 4])  # zwróci [2, 4]
    """
    return [x for x in data if x % 2 == 0]


def sum_data(data):
    """
    Sumuje wszystkie liczby z przekazanej listy 'data' i zwraca wynik.
    Przykład:
        sum_data([1, 2, 3])  # zwróci 6
    """
    return sum(data)
