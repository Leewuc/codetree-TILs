n,b=map(int,input().split())
table=[tuple(map(int,input().split())) for _ in range(n)]
table.sort(key=lambda x: x[0]+x[1])
ans=0
for i in range(n):
    price=0
    for j in range(n):
        price+=table[j][1]
        if i==j:
            price+=table[j][0]//2
        else:
            price+=table[j][0]
        if price<=b:
            ans=max(ans,j+1)
        else:
            break
print(ans)