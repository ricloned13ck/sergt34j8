import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

R2, G2, B2 = 7, 11, 7

def calculate_P_k(R2, G2, B2):
    P_values = []
    for k in range(R2 + 1):
        ans = ((math.factorial(G2 + B2) / (math.factorial(G2 + B2 - k) * math.factorial(k))) *
               (math.factorial(R2) / (math.factorial(k) * math.factorial(R2 - k)))) / \
              (math.factorial(R2 + G2 + B2) / (math.factorial(G2 + B2) * math.factorial(R2)))
        P_values.append(ans)
    return P_values

P_values = calculate_P_k(R2, G2, B2)
F_values = np.cumsum(P_values)
k_values = list(range(R2 + 1))

results_df = pd.DataFrame({"k": k_values, "P(k)": P_values, "F(k)": F_values})

plt.step(results_df["k"], results_df["F(k)"], where='post', color='black')
plt.xlabel('k')
plt.ylabel('F(k)')
plt.title('Функция распределения F(k) для числа красных шаров')
plt.ylim(0, 1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

print(results_df)