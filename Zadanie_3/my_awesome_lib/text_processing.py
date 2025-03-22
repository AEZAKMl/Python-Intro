def reverse_text(text):
    """
    Zwraca ciąg znaków 'text' odwrócony od końca.
    Przykład:
        reverse_text("Python")  # zwróci "nohtyP"
    """
    return text[::-1]


def count_words(text):
    """
    Liczy liczbę słów w podanym ciągu 'text'. Słowa oddzielone są spacjami.
    Przykład:
        count_words("Hello world!")  # zwróci 2
    """
    return len(text.split())
