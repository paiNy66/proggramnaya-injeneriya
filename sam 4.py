def get_sublist(tpl, element):
    if element not in tpl:
        return ()

    indices = [i for i, x in enumerate(tpl) if x == element]

    if len(indices) == 1:
        return tpl[indices[0]:]

    return tpl[indices[0]:indices[1] + 1]


print(get_sublist((1, 2, 3), 8))
print(get_sublist((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(get_sublist((1, 2, 8, 5, 1, 2, 9), 8))