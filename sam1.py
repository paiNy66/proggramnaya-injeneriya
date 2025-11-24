def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

fibonacci_200 = None
for i, num in enumerate(fib(200), 1):
    if i == 200:
        fibonacci_200 = num
        print(f"Число Фибоначчи №200: {fibonacci_200}")