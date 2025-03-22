import unittest
from my_awesome_lib import data_utils


class TestDataUtils(unittest.TestCase):
    def test_filter_even_normal(self):
        # Przykładowe dane – lista zawiera zarówno liczby parzyste, jak i nieparzyste
        self.assertEqual(data_utils.filter_even([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_filter_even_edge_empty(self):
        # Przypadek brzegowy: pusta lista powinna zwrócić pustą listę
        self.assertEqual(data_utils.filter_even([]), [])

    def test_filter_even_edge_all_odd(self):
        # Przypadek brzegowy: lista zawierająca tylko liczby nieparzyste
        self.assertEqual(data_utils.filter_even([1, 3, 5]), [])

    def test_filter_even_error_wrong_type(self):
        # Przykład błędnego użycia: elementy nie będące liczbami spowodują błąd (TypeError)
        with self.assertRaises(TypeError):
            data_utils.filter_even(['a', 'b', 'c'])

    def test_sum_data_normal(self):
        # Suma zwykłej listy liczb
        self.assertEqual(data_utils.sum_data([1, 2, 3]), 6)

    def test_sum_data_edge_empty(self):
        # Przypadek brzegowy: suma pustej listy to 0
        self.assertEqual(data_utils.sum_data([]), 0)

    def test_sum_data_edge_negative(self):
        # Lista zawierająca liczby ujemne
        self.assertEqual(data_utils.sum_data([-1, -2, -3]), -6)

    def test_sum_data_error_wrong_type(self):
        # Podanie listy z nie-liczbowymi elementami powinno podnieść błąd (TypeError)
        with self.assertRaises(TypeError):
            data_utils.sum_data([1, '2', 3])


if __name__ == '__main__':
    unittest.main()
