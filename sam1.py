data = input("Введите числа через пробел: ")
numbers_list = list(map(int, data.split()))
numbers_tuple = tuple(numbers_list)

print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)