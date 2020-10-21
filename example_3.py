print('Enter number:')
x = input()
res = 0
x = int(x)
sums = 0
for i in range(1, int(x)):

    if x % i == 0:
        for j in range(1, i):
            if i % j == 0:
                sums += 1
        if sums > 2:
            continue
        else:
            res = i
        sums = 0

print(res)
