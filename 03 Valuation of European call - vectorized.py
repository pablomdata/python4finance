#
# Monte Carlo valuation of European call options with NumPy
# mcs_vector_numpy.py
# https://github.com/yhilpisch/py4fi

import numpy as np
from time import time

np.random.seed(1234)
t0 = time()

# Parameters
S0 = 100.
K = 105.
T = 1.0
r = 0.05
sigma = 0.2
M = 50
dt = T / M
n_paths = 250000 * 2

# Simulating n_paths paths with M time steps
S = np.zeros((M + 1, n_paths))
S[0] = S0
for t in range(1, M + 1):
    z = np.random.standard_normal(n_paths)  # pseudo-random numbers
    z -= z.mean()  # corrects 1st moment
    z /= z.std()  # corrects 2nd moment
    S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)
    # vectorized operation per time step over all paths

# Calculating the Monte Carlo estimator
C0 = np.exp(-r * T) * np.sum(np.maximum(S[-1] - K, 0)) / n_paths

# Results output
tnp1 = time() - t0
print("European Option Value %7.3f" % C0)
print("Duration in Seconds   %7.3f" % tnp1)

# EXERCISE
# Implement a loop-free version taking the log on both sides and using a telescopic sum