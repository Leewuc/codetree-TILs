n = int(input())
def oou(m):
    if m == 1 or m == 2:
        return m
    elif m % 2 == 0:
        for i in range(0,m,2):
            m += i
        return m
    else:
        for i in range(1,m,2):
            m += i
        return m
print(oou(n))