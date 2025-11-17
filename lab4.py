class NameTooLongError(Exception):
    pass

def validate_name_length(name):
    if len(name) > 10:
        raise NameTooLongError("Имя слишком длинное")
    else:
        print("Успешная регистрация")

validate_name_length("Михаил")
validate_name_length("Александрович")