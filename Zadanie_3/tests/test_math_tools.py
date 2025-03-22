import unittest
from my_awesome_lib import math_tools


class TestMathTools(unittest.TestCase):
    def test_subtract_normal(self):
        # Przykładowe odejmowanie
        self.assertEqual(math_tools.subtract(10, 3), 7)
        self.assertEqual(math_tools.subtract(5, 5), 0)

    def test_subtract_edge_negative(self):
        # Przypadki brzegowe z liczbami ujemnymi
        self.assertEqual(math_tools.subtract(-5, -3), -2)
        self.assertEqual(math_tools.subtract(0, 5), -5)

    def test_subtract_error_wrong_type(self):
        # Przykład błędnego użycia: odejmowanie przy użyciu nieprawidłowych typów
        with self.assertRaises(TypeError):
            math_tools.subtract("10", 3)

    def test_power_normal(self):
        # Potęgowanie w typowych przypadkach
        self.assertEqual(math_tools.power(2, 3), 8)
        self.assertEqual(math_tools.power(5, 0), 1)  # każda liczba do potęgi 0 to 1

    def test_power_edge_negative_exponent(self):
        # Ujemny wykładnik – wynik może być liczbą zmiennoprzecinkową
        self.assertAlmostEqual(math_tools.power(2, -3), 0.125)

    def test_power_edge_fractional(self):
        # Test potęgowania liczb zmiennoprzecinkowych
        self.assertAlmostEqual(math_tools.power(4.0, 0.5), 2.0)

    def test_power_error_wrong_type(self):
        # Przykład błędnego użycia: nieprawidłowy typ wykładnika
        with self.assertRaises(TypeError):
            math_tools.power(2, "3")


if __name__ == '__main__':
    unittest.main()
