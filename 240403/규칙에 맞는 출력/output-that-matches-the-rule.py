n = int(input())
for i in range(1,n+1):
    for j in range(i+1,1,-1):
        print(n-j+2,end=" ")
    print()