def f(n):
    cnt = 0
    if n >= 1:
        if n % 2 == 0:
            n //= 2
            cnt += 1
            return cnt
        else:
            n //= 3
            cnt += 1
            return cnt
n = int(input())
print(f(n))