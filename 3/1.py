import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

# Данные задачи
R3 = 7  # количество красных шаров
G3 = 7  # количество зелёных шаров
B3 = 7  # количество синих шаров
total_balls = R3 + G3 + B3  # общее количество шаров

# Функция для вычисления вероятности P(k)
def probability_k(k, R3, total_balls):
    if k < R3:
        return 0  # Если k меньше, чем количество красных шаров, вероятность нулевая
    return (comb(k - 1, R3 - 1) * comb(total_balls - k, total_balls - R3 - k)) / comb(total_balls, R3)

# Рассчитаем P(k) для значений k от R3 до total_balls
k_values = np.arange(R3, total_balls + 1)
p_k_values = [probability_k(k, R3, total_balls) for k in k_values]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(k_values, p_k_values, marker='o', linestyle='-', label="P(k)")
plt.title("Вероятность P(k) полного извлечения красных шаров к эксперименту k")
plt.xlabel("Число экспериментов k")
plt.ylabel("P(k)")
plt.legend()
plt.grid()
plt.show()