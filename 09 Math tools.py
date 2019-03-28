import matplotlib.pyplot as plt
import numpy as np

# ## Approximation

def f(x):
    return np.sin(x) + 0.5 * x

x = np.linspace(-2 * np.pi, 2 * np.pi, 50)

plt.plot(x, f(x), 'b')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

# ### Regression

# #### Linear regresion

reg = np.polyfit(x, f(x), deg=1)
ry = np.polyval(reg, x)

plt.plot(x, f(x), 'b', label='f(x)')
plt.plot(x, ry, 'r.', label='regression')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

# ## Higher order polynomials
reg = np.polyfit(x, f(x), deg=5)
ry = np.polyval(reg, x)

plt.plot(x, f(x), 'b', label='f(x)')
plt.plot(x, ry, 'r.', label='regression')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

np.allclose(f(x), ry) # check if are numerically identical (change deg to 7 to get true)

np.sum((f(x) - ry) ** 2) / len(x)

# ### Constrained Optimization

# function to be minimized
# EXAMPLE
# An investor wants to maximize the expected utility by investing in two risky securities
# a,b that cost 10 today. After one year, on state u they get payoffs (15,5) and on state
# d they get payoffs (5,12). The budget of the investor is 100 and has an utility function
# utility(wealth) = sqrt(wealth)

def Eu(p):
    a, b = p
    return -(0.5 * np.sqrt(a * 15 + b * 5) + 0.5 * np.sqrt(a * 5 + b * 12))

# constraints
cons = ({'type': 'ineq', 'fun': lambda p: 100 - p[0] * 10 - p[1] * 10})
  # budget constraint
bnds = ((0, 1000), (0, 1000))  # uppper bounds large enough


result = spo.minimize(Eu, [5, 5], method='SLSQP',bounds=bnds, constraints=cons)

result['x']@[10,10] # Check if the investor depletes budget
-result['fun']

# ## Integration
import scipy.integrate as sci

def f(x):
    return np.sin(x) + 0.5 * x

a = 0.5  # left integral limit
b = 9.5  # right integral limit
x = np.linspace(0, 10)
y = f(x)

sci.fixed_quad(f, a, b)[0] # Fixed Gaussian quadrature rule

sci.quad(f, a, b)[0] # Adaptive quadrature

sci.romberg(f, a, b)


# ### Integration by Simulation (compare with values above)

# Monte Carlo integration: simulate a path, sum the function values, average
for i in range(1, 20):
    np.random.seed(1000)
    x = np.random.random(i * 10) * (b - a) + a
    print(np.sum(f(x)) / len(x) * (b - a))
