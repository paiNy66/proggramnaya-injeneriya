res = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]


sort_res = sorted(res)


best = sort_res[:3]


worst = sort_res[-3:]


from_10 = sort_res[sort_res.index(10.2):]

print(f"Три лучшие: {best}")
print(f"Три худшие: {worst}")
print(f"Все с 10: {from_10}")