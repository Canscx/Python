def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def sin(x, m):
    value = 0
    for i in range(1, m+1):
        value += ((-1) ** (i - 1)) * ((x ** (2*i-1)) / factorial(2*i-1))
    return value
print value