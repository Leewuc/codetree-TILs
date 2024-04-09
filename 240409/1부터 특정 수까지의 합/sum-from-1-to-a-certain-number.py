def div(n):
    ssum = 0
    for i in range(1,n+1):
        ssum += i
    return ssum // 10
n = int(input())
print(div(n))