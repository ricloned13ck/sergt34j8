import numpy as np
from scipy.special import erf

def phi(x):
    return 0.5 * (1 + erf(x / np.sqrt(2)))

R1, G1, B1 = 6, 10, 10
p = R1 / (R1 + G1 + B1)
q = 1 - p


for n in [25, 50, 100, 200, 400]:
    # Вычисление вероятности Pk(|m - np| <= R1)
    P_k = 2 * phi(R1 / np.sqrt(n * p * q))
    print(f"Вероятность того, что абсолютное число извлечений красных шаров отклонится от математического ожидания не более, чем на R1, для n = {n}: P(k) = {P_k:.5f}")