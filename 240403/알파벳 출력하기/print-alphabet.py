n = int(input())
pred = 65
for i in range(1,n+1):
    for j in range(i+1,1,-1):
        print(chr(pred),end="")
        pred+=1
        if pred > 90:
            pred = 65
    print()