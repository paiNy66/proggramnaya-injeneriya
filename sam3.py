def count_numbers(digits_string):
    count_dict = {}
    for char in digits_string:
        num = int(char)
        count_dict[num] = count_dict.get(num, 0) + 1

    sorted_items = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    top_three = dict(sorted_items[:3])

    return dict(sorted(top_three.items()))


result = count_numbers("123456789012345678901234")
print(result)