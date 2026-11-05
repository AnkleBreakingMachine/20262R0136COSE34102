
def factorial(n):
    if n < 0:
        raise ValueError("Negative input")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))