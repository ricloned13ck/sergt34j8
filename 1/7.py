import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

P_values = [0.7, 0.8, 0.9, 0.95, 0.99]
N1 = 26
p = 6/26

# n P(X >= N1) >= P
def find_min_n(target_prob, N1, p):
    n = N1
    while True:
        probability = 1 - stats.binom.cdf(N1 - 1, n, p)
        if probability >= target_prob:
            return n
        n += 1

n_values = [find_min_n(P, N1, p) for P in P_values]

print("P(k)   n")
for P, n in zip(P_values, n_values):
    print(f"{P:.2f}   {n}")
plt.plot(P_values, n_values, marker='o', linestyle='-', color='black')
plt.xlabel('P(k)')
plt.ylabel('n')
plt.title('Зависимость минимально необходимого числа испытаний n от вероятности P(k)')
plt.grid(True)

plt.show()
