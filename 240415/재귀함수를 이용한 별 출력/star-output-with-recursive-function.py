def p_s(n):
    if n == 0:
        return
    p_s(n-1)
    print("*" * n)
n = int(input())
p_s(n)