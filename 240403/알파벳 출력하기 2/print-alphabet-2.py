n = int(input())
pred = 65
for i in range(n):
    print("  "*i,end="")
    for j in range(n-i):
        print(chr(pred),end=" ")
        pred += 1
        if pred > 90:
            pred = 65
    print()