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