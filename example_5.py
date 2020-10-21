m = 101
s = 0
ss = 0
for i in range(1, m):
    s += i * i
for j in range(1, m):
    ss += j
s = ss*ss-s
print(s)
