import numpy as np


liczby = []
for i in range(6):
    liczby.append(int(input(f"Podaj liczbę {i+1}: ")))

print(f"Twój los: {liczby}")

wylosowane = np.random.choice(range(1, 50), 6, replace=False)  # choice - daje możliwośc wyłączenia powtórek
n = 0
for i in wylosowane:
    if i in liczby:
        n += 1
print(f"Wyniki losowania: {wylosowane},\nIlość trafień: {n}")

