import unittest
from my_awesome_lib import text_processing


class TestTextProcessing(unittest.TestCase):
    def test_reverse_text_normal(self):
        # Odwracanie typowego tekstu
        self.assertEqual(text_processing.reverse_text("Python"), "nohtyP")
        self.assertEqual(text_processing.reverse_text("ABC"), "CBA")

    def test_reverse_text_edge_empty(self):
        # Przypadek brzegowy: pusty tekst powinien zwrócić pusty tekst
        self.assertEqual(text_processing.reverse_text(""), "")

    def test_reverse_text_edge_unicode(self):
        # Test dla tekstu zawierającego znaki Unicode (np. polskie znaki)
        self.assertEqual(text_processing.reverse_text("zażółć"), "ćłóżąż")

    def test_reverse_text_error_none(self):
        # Podanie None powinno spowodować błąd (TypeError)
        with self.assertRaises(TypeError):
            text_processing.reverse_text(None)

    def test_count_words_normal(self):
        # Liczenie słów w typowym zdaniu
        self.assertEqual(text_processing.count_words("Hello world!"), 2)
        self.assertEqual(text_processing.count_words("Jeden dwa trzy"), 3)

    def test_count_words_edge_empty(self):
        # Pusty ciąg znaków – wynik powinien być 0
        self.assertEqual(text_processing.count_words(""), 0)

    def test_count_words_edge_extra_spaces(self):
        # Przypadek, gdy tekst zawiera wiele spacji między słowami
        self.assertEqual(text_processing.count_words("  Jeden   dwa   trzy  "), 3)

    def test_count_words_error_none(self):
        # Podanie None jako tekstu powinno wywołać błąd (AttributeError lub TypeError)
        with self.assertRaises(AttributeError):
            text_processing.count_words(None)


if __name__ == '__main__':
    unittest.main()
