i = 1
j = 1
sums = 0

while i < 10:
    if i % 2 == 0:  # even and odd
        sums += i

    # print(i)
    i += j
    j = i - j

print('Sum of fibonacci odd numbers:{}'.format(sums))
