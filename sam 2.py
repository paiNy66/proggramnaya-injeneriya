def remove_first_occurrence(tpl, element):
    if element not in tpl:
        return tpl

    lst = list(tpl)
    lst.remove(element)
    return tuple(lst)


print(remove_first_occurrence((1, 2, 3), 1))
print(remove_first_occurrence((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_first_occurrence((2, 4, 6, 6, 4, 2), 9))