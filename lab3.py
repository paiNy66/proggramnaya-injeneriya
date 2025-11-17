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