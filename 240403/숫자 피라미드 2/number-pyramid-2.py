n = int(input())
pred = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(pred,end=" ")
        pred += 1
    print()