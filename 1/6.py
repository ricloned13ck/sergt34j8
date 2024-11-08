import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

# Данные задачи
R1 = 6
G1 = 10
B1 = 10
n = 1000

p = R1 / (R1 + G1 + B1)
q = 1 - p
M_k = n * p
P_values = [0.7, 0.8, 0.9, 0.95, 0.99]

results = []
for P in P_values:
    x = norm.ppf((1 + P) / 2)  # аргумент функции Лапласа для данной вероятности
    epsilon = x * np.sqrt(n * p * q)
    interval = (M_k - epsilon, M_k + epsilon)
    results.append({"P(k)": P, "ε": epsilon, "Interval": interval})

results_df = pd.DataFrame(results)
print(results_df)
