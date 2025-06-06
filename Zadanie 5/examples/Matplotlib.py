
            ### Matplotlib (oraz numpy) ###
### Przedstawienie dwóch najczęstszych typów wykresów ###

# Ładujemy moduł matplotlib oraz numpy (jeden do wykresów/drugi do obliczeń)
import matplotlib.pyplot as plt
import numpy as np

#   Liniowy wykres sin(x):

x = np.linspace(0, 2*np.pi, 200)        # 200 punktów  w przedziale [0,2)
plt.plot(x, np.sin(x), label="sin(x)")      # Tworzymy Okno przedstawiające wykres naszej "Sinusoidy"
plt.title("Sinusoida")
plt.xlabel("x"); plt.ylabel("sin(x)")
plt.legend(); plt.show()

#   Wykres punktowy(scatter):

np.random.seed(0)                                       # Ustalamy nasz RNG seed
xs, ys = np.random.randn(30), np.random.randn(30)       # 30 losowych punktów jako dane do rozrzutu
plt.scatter(xs, ys)                                     # Wizualizacja naszego rozkładu punktów na płaszczyźnie
plt.title("Przykładowy scatter")
for i, (xi, yi) in enumerate(zip(xs, ys)):              # Pętla dodająca numer do każdego punktu
    plt.text(xi, yi, str(i))
plt.show()                                              # Wyświetlenie wykresu
