n = int(input())
pred = 65
for i in range(n):
    for j in range(n):
        print(chr(pred),end="")
        pred += 1
    print()