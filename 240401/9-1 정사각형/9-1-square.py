n = int(input())
pred = 9
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(pred,end="")
        pred -= 1
        if pred < 1:
            pred = 9
    print()