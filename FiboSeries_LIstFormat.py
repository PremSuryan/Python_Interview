def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example: Generate Fibonacci series with 10 terms
n_terms = 10
result = fibonacci_series(n_terms)
print(result)
