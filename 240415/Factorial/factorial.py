n = int(input())
def fac(m):
    if m == 0 or m == 1:
        return 1
    else:
        return fac(m-1) * m
print(fac(n))