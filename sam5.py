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

