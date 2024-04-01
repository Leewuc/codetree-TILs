n = int(input())
pred = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(pred,end="")
            pred += 1
    else:
        for j in range(n,0,-1):
            print(pred-1,end="")
            pred -= 1
    print()