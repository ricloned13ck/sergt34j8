import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom

def P_k(k, n, p):
    mean = n * p
    std_dev = np.sqrt(n * p * (1 - p))
    return norm.pdf(k, mean, std_dev)

def calculate_probabilities(n):
    R1, G1, B1 = 6, 10, 10
    p = R1 / (R1 + G1 + B1)

    mean = n * p  # математическое ожидание
    variance = n * p * (1 - p)  # дисперсия
    std_dev = np.sqrt(variance)  # стандартное отклонение

    # Определяем 7 точек вокруг mean, откладывая шаги ±1sqrt, ±2sqrt, ±3sqrt
    k_values = [
        mean - 3 * std_dev, mean - 2 * std_dev, mean - 1 * std_dev, mean,
        mean + 1 * std_dev, mean + 2 * std_dev, mean + 3 * std_dev
    ]
    P_values = [P_k(k, n, p) for k in k_values]

    for k, P in zip(k_values, P_values):
        print(f"k = {k:.2f}, P(k) = {P:.5f}")

    plot_stick_bars(n, p, k_values, P_values)


def plot_stick_bars(n, p, k_values, P_values):
    k_range = np.arange(0, n + 1)
    # Биномиальные вероятности для каждого k в диапазоне
    binom_probs = [binom.pmf(k, n, p) for k in k_range]

    plt.figure(figsize=(10, 6))
    plt.stem(k_range, binom_probs, basefmt=" ", linefmt="gray", markerfmt="D",
             label="Биномиальное распределение (палочки)")
    plt.plot(k_values, P_values, 'o-', color='black', label="Теоретическая огибающая (Муавр-Лаплас)")

    plt.xlabel("k (Число красных шаров)")
    plt.ylabel("Вероятность P(k)")
    plt.title(f"n = {n}")
    plt.legend()
    plt.grid(True)
    plt.show()


n = 400
calculate_probabilities(n)