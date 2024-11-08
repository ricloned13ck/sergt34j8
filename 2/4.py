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

expected_value = sum(k * P for k, P in zip(k_values, P_values))
expected_value_k2 = sum((k ** 2) * P for k, P in zip(k_values, P_values))

variance = expected_value_k2 - (expected_value ** 2)
print(f"Дисперсия = {variance:.5f}")
