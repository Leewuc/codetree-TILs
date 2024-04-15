def pp(n):
    if n == 1:
        return 1
    return pp(n-1) + n
n = int(input())
print(pp(n))