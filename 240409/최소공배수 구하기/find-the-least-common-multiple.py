def lcm(n, m):
    return (n * m) // gcd(n, m)

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

n, m = map(int, input().split())
print(lcm(n, m))