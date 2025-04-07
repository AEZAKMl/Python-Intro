
import numpy as np
import pandas as pd

from pymcdm.methods import TOPSIS, SPOTIS

# Macierz decyzyjna (4 alternatywy, 4 kryteria)

decision_matrix = np.array([
    [250, 16, 12, 5],
    [200, 20, 8, 3],
    [300, 12, 16, 4],
    [275, 18, 10, 2]
])

# Wektory wag (suma wag = 1)
weights = np.array([0.4, 0.3, 0.2, 0.1])

# Określenie typów kryteriów jako napisy:
# "max" – kryterium do maksymalizacji, "min" – kryterium do minimalizacji.
criteria = ["max", "max", "min", "min"]

# Konwersja kryteriów na format numeryczny dla SPOTIS:
# wartość 1 oznacza maksymalizację ("max"), a -1 minimalizację ("min")
criteria_numeric = np.array([1 if crit == "max" else -1 for crit in criteria])

def min_max_normalize(matrix, criteria):
    """
    Normalizuje macierz decyzyjną kolumna po kolumnie.
    Dla kryteriów 'max' skaluje wartości, tak by minimum było 0, a maksimum 1.
    Dla kryteriów 'min' – odwraca skalę.
    """
    normalized = np.zeros(matrix.shape)
    for j in range(matrix.shape[1]):
        col = matrix[:, j]
        if criteria[j] == "max":
            normalized[:, j] = (col - col.min()) / (col.max() - col.min())
        else:
            normalized[:, j] = (col.max() - col) / (col.max() - col.min())
    return normalized

norm_matrix = min_max_normalize(decision_matrix, criteria)


bounds = np.array([(decision_matrix[:, j].min(), decision_matrix[:, j].max()) for j in range(decision_matrix.shape[1])])
def compute_ranking(scores):
    """
    Oblicza ranking dla alternatyw na podstawie tablicy ocen.
    Wynik to tablica, w której dla każdej alternatywy podana jest pozycja w rankingu.
    Alternatywa o najwyższej ocenie otrzymuje pozycję 1.
    """
    sorted_idx = np.argsort(-scores)  # indeksy posortowane malejąco wg oceny
    ranking = np.empty_like(sorted_idx)
    ranking[sorted_idx] = np.arange(1, len(scores) + 1)
    return ranking


# Wykorzystanie metod decyzyjnych

# Metoda TOPSIS
topsis = TOPSIS()
# Wynik metody TOPSIS to tablica z ocenami
topsis_scores = topsis(decision_matrix, weights, criteria)
# Obliczenie rankingu na podstawie ocen
topsis_ranking = compute_ranking(topsis_scores)

# Metoda SPOTIS – przekazujemy obliczone bounds jako argument
spotis = SPOTIS(bounds)
# Dla SPOTIS przekazujemy jako kryteria wersję numeryczną
spotis_scores = spotis(decision_matrix, weights, criteria_numeric)
spotis_ranking = compute_ranking(spotis_scores)


# Macierz decyzyjna oraz znormalizowana wersja
print("Macierz decyzyjna:")
print(decision_matrix)
print("\nZnormalizowana macierz decyzyjna (Min-Max):")
print(norm_matrix)

# Wynik TOPSIS
print("\nWyniki TOPSIS:")
print("Oceny (scores):", topsis_scores)
print("Ranking:", topsis_ranking)

# Wynik SPOTIS
print("\nWyniki SPOTIS:")
print("Oceny (scores):", spotis_scores)
print("Ranking:", spotis_ranking)


alternatives = ['Alternatywa 1', 'Alternatywa 2', 'Alternatywa 3', 'Alternatywa 4']
results_df = pd.DataFrame({
    'Alternatywa': alternatives,
    'TOPSIS Score': topsis_scores,
    'TOPSIS Ranking': topsis_ranking,
    'SPOTIS Score': spotis_scores,
    'SPOTIS Ranking': spotis_ranking
})

print("\nPorównanie wyników:")
print(results_df)


