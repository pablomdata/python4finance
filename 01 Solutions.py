# 1. Write a function to calculate factorial(n)
def factorial(n):
    acc = 1
    for i in range(1, n+1):
        acc *= i
    return acc
	
# 2. How can we calculate how many capital letters are in a string?
test = 'testStrinG'
cnt = 0
for letter in test:
    if letter == letter.upper():
        cnt += 1
print('There are {0} capital letters'.format(cnt))


# 3. Given a value and a list of coefficients, evaluate the polynomial determined by such coefficients.
def poly(x, coeffs):
    val = 0
    for i, coeff in enumerate(coeffs):
        val += coeff*x**i
    return val



