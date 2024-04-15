def div(a):
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] //= 2
    return a
n = int(input())
m = list(map(int,input().split()))
div(m)
for elem in m:
    print(elem,end=" ")