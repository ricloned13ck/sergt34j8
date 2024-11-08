import math

R2, G2, B2 = 7, 11, 7

for k in range(R2+1):
    ans = ((math.factorial(G2+B2)/(math.factorial(G2+B2-k)*math.factorial(k))) * (math.factorial(R2)/(math.factorial(k) * math.factorial(R2-k))))/ (math.factorial(R2+G2+B2)/(math.factorial(G2+B2) * math.factorial(R2)))

    print(f'k = {k}, P(k) = {ans:.20f}')