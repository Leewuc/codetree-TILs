n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [0,1,0,-1],[1,0,-1,0]
cnt = 0
ans = 0
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n
for i in range(n):
    for j in range(n):
        for dxs,dys in zip(dx,dy):
            nx,ny = i + dxs, j+ dys
            if in_range(nx,ny) and lst[nx][ny] == 1:
                cnt += 1
    if cnt >= 3:
        ans += 1    

print(ans)