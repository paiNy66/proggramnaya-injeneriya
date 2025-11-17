# Тема 10.
Отчет по Теме #10 выполнил(а):
- Силантьев Филат Юрьевич
- ИВТ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | +  | + | 
| Задание 2 | +  | + | 
| Задание 3 | +  | + | 
| Задание 4 | +  | + | 
| Задание 5 | +  | + | 
знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Лабораторная работа №1
### Написать программу, которая считает числа Фибоначчи для 100 без декоратора и с декоратором @lru_cache, посмотреть на разницу во времени.


```
from functools import lru_cache
import time

def fib_without_cache(n):
    if n < 2:
        return n
    return fib_without_cache(n-1) + fib_without_cache(n-2)

@lru_cache(maxsize=None)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n-1) + fib_with_cache(n-2)

start = time.time()
result1 = fib_without_cache(35)
end = time.time()
print(f"Без кэша: {result1}, время: {end - start:.4f} сек")

start = time.time()
result2 = fib_with_cache(100)
end = time.time()
print(f"С кэшем: {result2}, время: {end - start:.4f} сек")

```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_10/Theme10_lab1.jpg)

## Выводы

fib_without_cache — рекурсивная функция без кэширования, работает медленно
@lru_cache — декоратор, кэширует результаты вызовов, ускоряет выполнение
time.time() — используется для замера времени выполнения функций

## Лабораторная работа №2
### Написать декоратор для функции, который проверяет, что возраст больше 0 и меньше 130. Обрабатывать только первые два аргумента.


```
def validate_age(func):
    def wrapper(*args):
        name, age = args[:2]
        if not (0 < age < 130):
            raise ValueError("Недопустимый возраст")
        return func(*args)
    return wrapper

@validate_age
def print_user_info(name, age):
    print(f"Имя: {name}, Возраст: {age}")

print_user_info("Илья", 25)

```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_10/Theme10_lab2.jpg)

## Выводы

validate_age — декоратор, проверяет возраст
args[:2] — берёт только первые два аргумента
raise ValueError — вызывает исключение при неверном возрасте


## Лабораторная работа №3
### Обработать исключения, если в функцию передаётся не integer, а string. Использовать try/except/finally.


```
def safe_int_conversion(func):
    def wrapper(*args):
        try:
            return func(*args)
        except TypeError as e:
            print(f"Ошибка типа: {e}")
        except Exception as e:
            print(f"Общая ошибка: {e}")
        finally:
            print("Проверка завершена")
    return wrapper

@safe_int_conversion
def process_data(value):
    return int(value)

process_data("123")
process_data("abc")

```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_10/Theme10_lab3.jpg)

## Выводы

safe_int_conversion — декоратор для обработки исключений
try/except — перехватывает ошибки при преобразовании типа
finally — выполняется всегда, независимо от ошибок

## Лабораторная работа №4
### Написать собственное исключение, если имя длиннее 10 символов.


```
class NameTooLongError(Exception):
    pass

def validate_name_length(name):
    if len(name) > 10:
        raise NameTooLongError("Имя слишком длинное")
    else:
        print("Успешная регистрация")

validate_name_length("Михаил")
validate_name_length("Александрович")
```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_10/Theme10_lab4.jpg)

## Выводы

NameTooLongError — пользовательское исключение
len(name) > 10 — проверка длины имени
raise — выброс исключения при нарушении условия

## Лабораторная работа №5
### Создать декоратор-логгер с методами __init__ и __call__, выводящий логи в консоль.


```
class Logger:
    def __init__(self, func):
        print('> Класс Logger метод __init__ успешный запуск')
        self.func = func

    def __call__(self):
        print('> Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасного выключения')

@Logger
def site():
    print('Усердная работа сайта')

site()
```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_10/Theme10_lab5.jpg)

## Выводы

init — вызывается при создании декоратора
call — вызывается при вызове функции
self.func.name — получает имя оборачиваемой функц

## Самостоятельная работа №1
### Создать декоратор для измерения времени выполнения функции

```
import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"\nВремя выполнения: {end - start:.4f} секунд")
        return result
    return wrapper

@timer
def fibonacci():
    fib1 = fib2 = 1
    print(fib1, fib2, end=' ')
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

if __name__ == '__main__':
    fibonacci()
```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_10/Theme10_sam1.jpg)

## Выводы

timer — декоратор для измерения времени выполнения
start = time.time() — фиксирует время начала выполнения
end = time.time() — фиксирует время окончания выполнения
{end - start:.4f} — вычисляет и форматирует время выполнения

## Самостоятельная работа №2
### Обработать исключение при чтении пустого файла

```
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                raise Exception("файл пустой")
            print(content)
    except Exception as e:
        print(e)

read_file("empty.txt")
read_file("with_content.txt")
```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_10/Theme10_sam2.jpg)

## Выводы

with open — безопасное открытие файла
content.strip() — проверка на пустоту содержимого
raise Exception — вызов исключения при пустом файле
except Exception — перехват всех исключений

## Самостоятельная работа №3
### Функция сложения с обработкой неверного типа данных

```
def add_two():
    try:
        num = float(input("Введите число: "))
        result = 2 + num
        print(f"Результат: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

add_two()
add_two()
```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_10/Theme10_sam3.jpg)

## Выводы

float(input()) — попытка преобразовать ввод в число
except ValueError — перехват ошибки преобразования типа
2 + num — сложение с числом 2
print(f"Результат: {result}") — вывод результата при успехе

## Самостоятельная работа №4
### Создать собственный декоратор для двух функций

```
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
```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_10/Theme10_sam4.jpg)

## Выводы

Counter — класс-декоратор с счетчиком вызовов
self.count += 1 — увеличивает счетчик при каждом вызове
call — делает экземпляр вызываемым как функцию
self.func.name — получает имя оригинальной функции

## Самостоятельная работа №5
### Создать собственное исключение для использования в двух местах

```
class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Число не может быть отрицательным")
    return number

def calculate_square_root(number):
    try:
        checked_num = check_positive(number)
        result = checked_num ** 0.5
        print(f"Квадратный корень: {result}")
    except NegativeNumberError as e:
        print(f"Ошибка: {e}")

def process_age(age):
    try:
        checked_age = check_positive(age)
        print(f"Возраст принят: {checked_age}")
    except NegativeNumberError as e:
        print(f"Ошибка возраста: {e}")

calculate_square_root(25)
calculate_square_root(-9)
process_age(20)
process_age(-5)
```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_10/Theme10_sam5.jpg)

## Выводы

NegativeNumberError — пользовательский класс исключения
check_positive — функция проверки положительности числа
raise NegativeNumberError — выброс исключения при отрицательном числе
except NegativeNumberError — перехват пользовательского исключения
