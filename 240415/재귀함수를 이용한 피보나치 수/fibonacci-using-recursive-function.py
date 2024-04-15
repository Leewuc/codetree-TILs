n = int(input())
def pibo(m):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    return pibo(n-1) + pibo(n-2)
print(pibo(n))