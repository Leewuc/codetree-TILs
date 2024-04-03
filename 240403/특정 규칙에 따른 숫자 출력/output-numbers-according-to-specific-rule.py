n = int(input())
pred = 1
for i in range(n):
    print("  "*i,end="")
    for j in range(n-i):
        print(pred,end=" ")
        pred += 1
        if pred > 9:
            pred = 1
    print()