class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Функция {self.func.__name__} вызвана {self.count} раз")
        return self.func(*args, **kwargs)

@Counter
def greet(name):
    print(f"Привет, {name}!")

@Counter
def multiply(a, b):
    result = a * b
    print(f"Результат умножения: {result}")
    return result

greet("Анна")
greet("Петр")
multiply(3, 4)
multiply(5, 6)