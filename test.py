import numpy as np

# Given constant lambda
lmbda = 10000 / 71 # Calculated lambda

# Loop over the range of k from 90 to 300 and calculate a for each k
results = []
for k in range(90, 301):
    # Logarithmic calculations to avoid overflow
    lmbda_power_k = k * np.log(lmbda)  # log(lambda^k)
    log_k_factorial = sum(np.log(i) for i in range(1, k + 1))  # log(k!)
    log_a = lmbda_power_k - log_k_factorial - lmbda  # log of the result

    # Converting back from log-space
    a = np.exp(log_a)
    results.append((k, a))

# Display the results in fixed-point notation

max_k, max_a =0,0
for k, a_value in results:
    print(f"k = {k}, a = {a_value:.20f}")
    if max_a <= a_value:
        max_a = a_value
        max_k = k

print(max_k, max_a)
