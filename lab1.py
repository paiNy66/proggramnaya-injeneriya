from functools import lru_cache
import time

def fib_without_cache(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

@lru_cache(maxsize=None)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n-1) + fib_with_cache(n-2)

start = time.time()
result1 = fib_without_cache(100)
end = time.time()
print(f"Без кэша: {result1}, время: {end - start:.4f} сек")

start = time.time()
result2 = fib_with_cache(100)
end = time.time()
print(f"С кэшем: {result2}, время: {end - start:.4f} сек")