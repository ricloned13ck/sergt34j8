import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

R1 = 6
G1 = 10
B1 = 10
n = 1000

p = R1 / (R1 + G1 + B1)
q = 1 - p

epsilons = np.array([1e-1, 1e-2, 1e-3])
probabilities = 2 * norm.cdf(epsilons * np.sqrt(n) / np.sqrt(p * q)) - 1

results_df = pd.DataFrame({"ε": epsilons, "P(k)": probabilities})
print(results_df)

plt.plot(epsilons, probabilities, marker='o', linestyle='-', color='black')
plt.xlabel(r'$\varepsilon$')
plt.ylabel(r'$P(k)$')
plt.title('Зависимость вероятности от ε')
plt.grid(True)
plt.show()