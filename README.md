# Тема 11.
Отчет по Теме #11 выполнил(а):
- Силантьев Филат Юрьевич
- ИВТ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | +  | + | 
| Задание 2 | +  | + | 
| Задание 3 | +  | 
| Задание 4 | +  | 
| Задание 5 | +  | 
знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Самостоятельная работа №1
### Генератор чисел Фибоначчи


```
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

```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/main/Theme11_sam1.jpg)

## Выводы

fib(n) - функция-генератор чисел Фибоначчи
yield a - возврат текущего числа без завершения функции
Число Фибоначчи №200: 453973694165307953197296969697410619233826

## Самостоятельная работа №2
### Запись чисел Фибоначчи в файл


```
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

```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/main/Theme11_sam2.jpg)

## Выводы

with open("fib.txt", "w") as file: - открытие файла для записи
file.write(f"Число Фибоначчи №{i}: {num}\n") - запись каждого числа в файл
Числа Фибоначчи записаны в файл fib.txt

## Лабораторная работа №1
### Простой итератор


```
numbers = [0, 1, 2, 3, 4, 5]
for item in numbers:
    print(item)

```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/main/Theme11_lab1.jpg)

## Выводы

numbers = [0, 1, 2, 3, 4, 5] - создание списка
for item in numbers: - автоматическое использование итератора

## Лабораторная работа №2
### Простой итератор


```
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

```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/main/Theme11_lab2.jpg)

## Выводы

class Counter: - создание класса-итератора
__iter__ и __next__ - обязательные методы для итератора

## Лабораторная работа №3
### Создание списка с помощью генераторного выражения


```
squares = [x**2 for x in range(1, 6)]
for square in squares:
    print(square)

```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/main/Theme11_lab3.jpg)

## Выводы

[x**2 for x in range(1, 6)] - генератор списка квадратов



## Лабораторная работа №4
### Создание генератора с помощью круглых скобок


```
(x**2 for x in range(1, 6)) - создание генераторного выражения
```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/main/Theme11_lab4.jpg)

## Выводы

(x**2 for x in range(1, 6)) - создание генераторного выражения

## Лабораторная работа №5
### Создание функции-генератора с использованием ключевого слова yield


```
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
```
### Результаты выполнения тестов.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/main/Theme11_lab5.jpg)

## Выводы

def countdown(n): - объявление функции-генератора
yield n - возврат значения без завершения функции
