c = 0

for i in range(2, 2000000):
    sums = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sums += 1
    if sums > 2:
        continue
    else:
        res = i
        c += res
print('sum={}'.format(c))
