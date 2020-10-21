c = 0

for i in range(2, 1000000):
    sums = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sums += 1
    if sums > 2:
        continue
    else:
        res = i
        c += 1
    print('{0} - {1}'.format(c, res))
    if c == 10001:
        break

