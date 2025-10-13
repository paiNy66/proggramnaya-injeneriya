l1 = [1, 1, 3, 3, 1]
l2 = [5, 5, 5, 5, 5, 5, 5]
l3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
def make_set(lst):
    res = set()
    for num in set(lst):
        cnt = lst.count(num)
        for i in range(1, cnt + 1):
            if i == 1:
                res.add(num)
            else:
                res.add(str(num) * i)
    return res
s1 = make_set(l1)
s2 = make_set(l2)
s3 = make_set(l3)

print(s1)
print(s2)
print(s3)