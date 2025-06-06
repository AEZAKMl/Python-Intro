
                            ### PyTorch ###
### Demonstracja prostych operacji tensorowych oraz mikro-workflow uczenia ###

# Ładujemy moduł PyTorch
import torch

# Tworzymy dwa losowe tensory należacę wartością od [0,1).
a = torch.rand(2, 3)          # tensor 2×3
b = torch.rand(2, 3)
c = a + b                     # Podstawowa arytmetyka na Tensorze czyli równoległe obliczenia
print("Suma\n", c)

#  Prosta regresja y ≈ 2x + 0.3
import torch.nn as nn
import torch.optim as optim

x = torch.randn(100, 1)       # 100 losowych wejść 1-wymiarowych
y = 2 * x + 0.3               # Generuje etykiety dla funkcji: "y = 2x + 0.3"

model = nn.Linear(1, 1)       # Najprostsza sieć do regresji 1 -> 1
loss_fn = nn.MSELoss()                            # Średni błąd kwadratowy
opt = optim.SGD(model.parameters(), lr=0.1)       # Optymalizator z krokiem lr=0.1

for epoch in range(200):      # Jest to nasza pętla treningowa na 200 epok
    opt.zero_grad()           # zerowanie gradientów
    y_hat = model(x)          # predykcja
    loss = loss_fn(y_hat, y)  # MSE
    loss.backward()           # oblicza gradienty
    opt.step()                # aktualizuje parametry

print("Wyuczone w, b:",       # Sprawdzamy czy nasze "w" i "b" zbliżają się do 2 oraz 0.3 i wypisujemy rezultat.
      model.weight.item(), model.bias.item())
