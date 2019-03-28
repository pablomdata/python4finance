# Monte Carlo valuation of European call options with pure Python
# mcs_pure_python.py
# https://github.com/yhilpisch/py4fi

from time import time
import numpy as np

np.random.seed(1234)
t0 = time()

# Parameters
S0 = 100.  # initial value
K = 105.  # strike price
T = 1.0  # maturity
r = 0.05  # risk-less short rate
sigma = 0.2  # volatility
M = 50  # number of time steps
dt = T / M  # length of time interval
n_paths = 250000  # number of paths

# Simulating n_paths paths with M time steps
S = []
for i in range(n_paths):
    path = []
    for t in range(M + 1):
        if t == 0:
            path.append(S0)
        else:
            z = np.random.standard_normal()
            St = path[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)
            path.append(St)
    S.append(path)

# Calculating the Monte Carlo estimator
C0 = np.exp(-r * T) * np.sum([np.maximum(path[-1] - K, 0) for path in S]) / n_paths

# Results output
tpy = time() - t0
print("European Option Value %7.3f" % C0)
print("Duration in Seconds   %7.3f" % tpy)
