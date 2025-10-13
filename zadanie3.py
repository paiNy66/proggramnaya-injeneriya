a = [12, 25, 3, 48, 71]
b = [5, 18, 40, 62, 98]
c = [4, 21, 37, 56, 84]

min_a = min(a)
min_b = min(b)
min_c = min(c)

max_a = max(a)
max_b = max(b)
max_c = max(c)


def plos(x, y, z):
    p = (x + y + z) / 2  #п
    return (p * (p - x) * (p - y) * (p - z)) ** 0.5

pl_min = plos(min_a, min_b, min_c)
pl_max = plos(max_a, max_b, max_c)

print(f"Площадь из минимальных: {pl_min:.2f}")
print(f"Площадь из максимальных: {pl_max:.2f}")