def maxi(n):
    for i in range(a):
        if n[i] < 0:
            n[i] = -n[i]
        else:
            n[i] = n[i]
    return n
a = int(input())
n = list(map(int,input().split()))
maxi(n)
for i in range(a):
    print(n[i],end=" ")