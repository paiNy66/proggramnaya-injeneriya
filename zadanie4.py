
g1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
g2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
g3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

r1 = [4 if x == 3 else x for x in g1 if x != 2]
r2 = [4 if x == 3 else x for x in g2 if x != 2]
r3 = [4 if x == 3 else x for x in g3 if x != 2]

print(r1)
print(r2)
print(r3)