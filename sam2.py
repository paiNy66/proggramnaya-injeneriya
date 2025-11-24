def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

with open("fib.txt", "w") as file:
    for i, num in enumerate(fib(200), 1):
        file.write(f"Число Фибоначчи №{i}: {num}\n")

print("Числа Фибоначчи записаны в файл fib.txt")