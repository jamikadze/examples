a=1
b=1
c=1
for c in range(1000):
    for b in range(c):
        for a in range(b):
            if a*a+b*b==c*c:
                if a + b + c == 1000:
                    print(a,b,c)

