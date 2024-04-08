n=int(input())
alist=[
    [0 for _ in range(n)]
    for _ in range(n)
    ]




for i in range(n):
    alist[i][0]=1
    alist[0][i]=1


for i in range(1,n):
    for j in range(1,n):
        alist[i][j]=alist[i-1][j]+alist[i][j-1]+alist[i-1][j-1]

for i in range(n):
    for j in range(n):
        print(alist[i][j],end=" ")
    print("")