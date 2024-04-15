n = int(input())
def suu(m):
    if m == 1:
        return 1
    if m == 2:
        return 2
    return suu(m//3) + suu(m-1)

print(suu(n))