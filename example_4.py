max = 100
for i in range(100, 10000):
    for j in range(100, 10000):
        mult = i * j
        str1 = str(mult)
        str2 = str1[::-1]

        if str2 == str1:
            if max < mult:
                max = mult
print(max)
