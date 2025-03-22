import unittest
from app import czy_email_poprawny
from app import oblicz_pole_trojkata
from app import przetworz_liste
from app import konwertuj_date
from app import czy_palindrom


class TestEmailValidation(unittest.TestCase):
    def setUp(self):
        # Poprawne adresy e-mail, które powinny przejść walidację
        self.poprawne = ["dorian@gmail.com", "kozlowski@xyz.pl"]

        # Niepoprawne adresy e-mail, które nie powinny przejść walidacji
        self.niepoprawne = ["@dorian.com", "dorian@kozlowski", "dorian.kozlowski", ""]

    def test_email_poprawny(self):
        # Testowanie poprawnych adresów e-mail
        for email in self.poprawne:
            with self.subTest(email=email):
                self.assertTrue(czy_email_poprawny(email))

    def test_email_niepoprawny(self):
        # Testowanie błędnych adresów e-mail
        for email in self.niepoprawne:
            with self.subTest(email=email):
                self.assertFalse(czy_email_poprawny(email))


class TestObliczeniaMatematyczne(unittest.TestCase):
    def test_dodatnie_wartosci(self):
        # Test z dodatnimi wartościami poprawnie obliczającymi pole
        self.assertEqual(oblicz_pole_trojkata(5, 5), 12.5)

    def test_zerowe_wartosci(self):
        # Test z zerowymi wartościami
        with self.assertRaises(ValueError):
            oblicz_pole_trojkata(5, 0)
        with self.assertRaises(ValueError):
            oblicz_pole_trojkata(0,3)

    def test_ujemne_wartosci(self):
        # Test z ujemnymi wartościami
        with self.assertRaises(ValueError):
            oblicz_pole_trojkata(-5, 5)
        with self.assertRaises(ValueError):
            oblicz_pole_trojkata(3, -2)


class TestPrzetwarzanieListy(unittest.TestCase):
    def setUp(self):
        # Lista z różnymi wartościami
        self.lista_z_wartosciami = [1, 2, 3, 4, 10, 7, 15, 8, 20, 9, 19]

        # Lista pusta - wynik pusty
        self.lista_pusta = []

        # Lista z wartościami nie spełniającymi warunku >= 10
        self.lista_bez_pasujacych = [1, 2, 3, 4, 7, 8, 9]

    def test_standardowe_dane(self):
        # Sprawdzanie poprawnego filtrowania i sortowania wartości >= 10
        wynik = przetworz_liste(self.lista_z_wartosciami)
        self.assertEqual(wynik, [10, 15, 19, 20])

    def test_pusta_lista(self):
        # Sprawdzanie reakcji na pustą listę
        wynik = przetworz_liste(self.lista_pusta)
        self.assertEqual(wynik, [])

    def test_brak_pasujacych_danych(self):
        # Sprawdzanie reakcji na wartości < 10
        wynik = przetworz_liste(self.lista_bez_pasujacych)
        self.assertEqual(wynik, [])


class TestKonwersjaDat(unittest.TestCase):
    def setUp(self):
        # Poprawne daty w różnych formatach
        self.poprawne = [
        ("21-03-2025", "2025/03/21"),
        ("05.03.2020", "2020/03/05"),
        ("03-05-2019", "2019/05/03"),
        ("03.05.2019", "2019/05/03"),
        ]

        # Błędne daty - niepoprawne formaty lub puste pole
        self.bledne = ["2025-03-21", "2025.03.21", ""]

    def test_standardowa_data(self):
        # Sprawdzanie konwersji poprawnych dat
        for data, oczekiwana in self.poprawne:
            with self.subTest(data=data):
                self.assertEqual(konwertuj_date(data), oczekiwana)


    def test_nieprawidlowa_data(self):
        # Sprawdzanie, czy są wyjątki dla niepoprawnych formatów
        for data in self.bledne:
            with self.subTest(data=data):
                with self.assertRaises(ValueError):
                    konwertuj_date(data)


class TestCzyPalindrom(unittest.TestCase):
    def setUp(self):
        # Lista tekstów - palindromów
        self.palindrom = [
            "kajak",
            "potop",
            "żartem w metraż",
            "kobyła ma mały bok",
            "a",
            ""
        ]

        # Lista tekstów - nie palindromów
        self.nie_palindrom = [
            "słoma",
            "palindrom"
        ]


    def test_palindrom(self):
        # Testowanie rozpoznawania palindromów
        for tekst in self.palindrom:
            with self.subTest(tekst=tekst):
                self.assertTrue(czy_palindrom(tekst))


    def test_nie_palindrom(self):
        #  Testowania rozpoznawania braku palindromów
        for tekst in self.nie_palindrom:
            with self.subTest(tekst=tekst):
                self.assertFalse(czy_palindrom(tekst))


if __name__ == '__main__':
    unittest.main()
