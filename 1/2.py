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

    mean = n * p #mat ojid
    std_dev = np.sqrt(n * p * (1 - p)) # otkl

    # k от max(0, mean - 3*std_dev) до mean + 3*std_dev и 7 точек
    k_min = max(0, mean - 3 * std_dev)
    k_max = mean + 3 * std_dev
    k_values = np.linspace(k_min, k_max, 7)
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


n = 50
calculate_probabilities(n)